from os.path import join
from django.http import JsonResponse
from log.models import RequestRecord, Action
from utils.tools import statisticData
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


def action_log():
    '''用户行为记录装饰器'''

    def inner(cls):
        class DecoratedClass(cls):
            action_mapping = {
                'BlogViewSet': {
                    'retrieve': Action.CLICK,
                    'reward': Action.REWARD,
                    'share': Action
                },
                'CollectionViewSet': {
                    'create': Action.COLLECT,
                    'destroy': Action.CANCEL_COLLECT
                },
                'LikeViewSet': {
                    'create': Action.DOCALL,
                    'destroy': Action.CANCEL_DOCALL,
                },
                'CommentViewSet': {
                    'create': Action.COMMENT,
                    'destroy': Action.CANCEL_COMMENT,
                }
            }

            def __getattribute__(self, action):
                attr = super().__getattribute__(action)
                action_class = cls.__name__
                if callable(attr) and action_class in self.action_mapping and action in self.action_mapping[
                    action_class]:
                    # 记录
                    def wrapped(request, *args, **kwargs):
                        res = attr(self, request, *args, **kwargs)
                        request_data = self.request.data or self.request.query_params
                        user = request.user if request.user.is_authenticated else None
                        uuid = request.COOKIES.get('uuid')
                        blog_id = request_data.get('blog_id')

                        Action.create(user, uuid, blog_id, self.action_mapping[action_class][action], 0)

                        return res

                    return wrapped

                return attr

        return DecoratedClass

    return inner
