from os.path import join
from apscheduler.scheduler import Scheduler
from django.http import JsonResponse
from article.models import Blog
from log.models import RequestRecord, Action
from utils.tools import statisticData
import json
import re
from django.core.cache import cache


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


# 定时任务
scheduler = Scheduler()


# 每一小时执行一次
# @scheduler.interval_schedule(seconds=3600)  # 3600
def update_top_k():
    # 刷新排行榜
    RequestRecord.stat_top()

    # 刷新后台的统计数据
    # drawPictureAndWriteToFile()

    # 定时更新请求的位置


def update_action_data():
    action_data = Action.summary()
    cache.set('action_data', action_data)


# @scheduler.interval_schedule(seconds=5)
def update_recommend_list():
    action_data = cache.get('action_data') or {}

    # 更新推荐列表
    user_recommend_queue = cache.get('user_recommend_queue')
    print(f'user_recommend_queue:{user_recommend_queue}')
    while user_recommend_queue:
        user = user_recommend_queue.pop()
        recommend_list = Blog.recommend(user, action_data)
        cache.set(f'{user}_recommend_list', recommend_list, 60)
        cache.set('user_recommend_queue', user_recommend_queue)


scheduler.add_interval_job(update_top_k, seconds=3600, max_instances=10)
#scheduler.add_interval_job(update_action_data, seconds=1800, max_instances=10)
#scheduler.add_interval_job(update_recommend_list, seconds=60, max_instances=10)

scheduler.start()
