from os.path import join
from apscheduler.schedulers.background import BackgroundScheduler
from django.http import JsonResponse
from blog.models import Blog
from log.models import RequestRecord, Action
from utils.tools import statisticData
import json
import re
import time
from django.core.cache import cache
from log.logger import logger


# 返回可视化的代码
def returnPicture(request):
    if request.method == 'POST':
        whichOne = request.POST.get('whichOne')  # 1代表月数据 2代表年数据
        with open(join('templates', f'demo{whichOne}.html'), 'r', encoding='utf8') as f:
            content = f.read().replace(
                '<script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>', '')
            div = re.search(r'<div.*div>', content).group()
            return JsonResponse({'div': div})  # ,'script':script
    return JsonResponse({'div': '数据请求失败!'})


# 绘制数据显示图标并将其写入文件
def drawPictureAndWriteToFile():
    for i in range(1, 3):
        statisticData(RequestRecord, i)  # 绘图1和图2
        with open(join('templates', f'demo{i}.html'), 'r', encoding='utf8') as f:
            content = f.read().replace(
                '<script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>', '')
            script = re.sub(
                r'(<div.*div>)|</script>|<script>|<!DOCTYPE html>|<html>|<head>|<meta charset="UTF-8">|<title>Awesome-pyecharts</title>|</head>|<body>|</body>|</html>',
                '', content)
        with open(join('static', 'js', f'demo{i}.js'), 'w+', encoding='utf8') as f:
            f.write(script)


# 用户行为记录
def action_log(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')
        cost_time = data.get('cost_time')
        blog = Blog.get_by_id(data.get('blog_id'))
        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        Action.create(user, _uuid, blog, action, cost_time)

        return JsonResponse({
            'code': '200',
            'msg': '响应成功!'
        })


# 创建异步调度器对象
scheduler = BackgroundScheduler()


# 更新排行榜
def update_top_k():
    logger.info('开始更新排行榜...')
    # 刷新排行榜
    RequestRecord.stat_top()
    logger.info('排行榜更新完成...')


# 更新用户行为数据
def update_action_data():
    action_data = Action.summary()
    cache.set('action_data', action_data)
    logger.info(f'对用户的行为数据进行了统计更新...')


# 更新推荐列表
def update_recommend_list():
    action_data = cache.get('action_data') or {}

    # 更新推荐列表
    user_recommend_queue = cache.get('user_recommend_queue')
    logger.info(f'待计算的用户推荐列表:[大小:{len(user_recommend_queue)}]:{user_recommend_queue}')
    t1 = time.time()
    while user_recommend_queue:
        t2 = time.time()
        if t2 - t1 > 150:
            logger.info(f'当前计算耗时超过150s,退出计算...')
            break
        user = user_recommend_queue.pop()
        recommend_list = Blog.recommend(user, action_data)
        t3 = time.time()
        logger.info(f'为用户[{user}]计算推荐列表耗时:{t3 - t2}...')
        cache.set(f'{user}_recommend_list', recommend_list)
        cache.set('user_recommend_queue', user_recommend_queue)
    logger.info(f'当前计算推荐列表结束，剩余{len(user_recommend_queue)}条待计算...')


scheduler.add_job(update_top_k, trigger='interval', seconds=3600, max_instances=10)
#scheduler.add_job(update_action_data, trigger='interval', seconds=1800, max_instances=10)
#scheduler.add_job(update_recommend_list, trigger='interval', seconds=300, max_instances=10)

scheduler.start()
