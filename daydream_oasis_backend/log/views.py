from os.path import join
from django.http import JsonResponse
from blog.models import Blog
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


