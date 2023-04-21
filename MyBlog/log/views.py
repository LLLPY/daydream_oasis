from os.path import join
from apscheduler.scheduler import Scheduler
from django.http import JsonResponse
from article.models import Blog
from log.models import RequestRecord, Action
from utils.tools import statisticData
import json
import re


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
@scheduler.interval_schedule(seconds=3600)  # 3600
def schedule_task():
    # 刷新排行榜
    RequestRecord.stat_top()

    # 刷新后台的统计数据
    # drawPictureAndWriteToFile()

    # 定时更新请求的位置


scheduler.start()
import time
def clocked(func):
    def clock(*args,**kwargs):
        time1=time.time()
        res=func(*args,**kwargs)
        time2=time.time()
        res['cost']=time2-time1
        return JsonResponse(res)
    return clock

from article.models import Blog,Search
@clocked
def test(request):
     # 关键词
    keyword = request.GET.get('keyword', '')[:20]
    category = request.GET.get('category', '')
    tag = request.GET.get('tag', '')

    # 获取关键词
    keyword_list = Search.get_keyword_list(keyword)
    if not keyword_list:

        # 首页
        search_list = Blog.objects.only('id', 'title', 'author', 'avatar', 'category', 'abstract','create_time')

        # 分类搜索
        if category:
            search_list = search_list.filter(category__title=category)

        # 标签搜索
        if tag:
            search_list = search_list.filter(tags__title__contains=tag)
        
        # 个性推荐
        user = request.user.id if request.user.is_authenticated else request.COOKIES.get('uuid', '-')
        # action_data = Action.summary()
        # search_list = Blog.recommend(user, search_list, action_data)
    else:
        search_list = Blog.search(keyword_list)


    return {
        'code': '200',
        'cost':0,
        'data':str([blog.to_dict(fields=['abstract']) for blog in search_list])
    }
