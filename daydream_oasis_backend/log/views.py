import datetime

from common.drf.response import SucResponse
from common.views import BaseViewSet
from django.db.models import Count
from log.models import Action
from log.serializers import ActionSerializer
from rest_framework.decorators import action
from utils import tools
from utils.cache import my_cache


class ActionViewSet(BaseViewSet):
    serializer_class = ActionSerializer
    queryset = Action.objects.all()

    @action(methods=['post'], detail=False)
    def upload_action(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=self.request.data, include_fields=[
                                        'blog_id', 'action', 'cost_time'])
        serialzer.is_valid(raise_exception=True)

        blog_id = serialzer.data.get('blog_id')
        action = serialzer.data.get('action')
        cost_time = serialzer.data.get('cost_time')

        action_obj = Action()
        action_obj.action = action
        action_obj.cost_time = cost_time
        action_obj.user = request.user if request.user.is_authenticated else None
        action_obj.uuid = request.COOKIES.get('uuid', '-')
        action_obj.blog_id = blog_id
        action_obj.save()

        return SucResponse('行为上传成功!')

    @my_cache()
    @action(methods=['get'], detail=False)
    def top_stat(self, request, *args, **kwargs):
        '''排行榜统计'''
        now = datetime.datetime.now()
        res = Action.objects.values('blog_id', 'blog__title').annotate(visit_count=Count('blog_id')).filter(
            action=Action.CLICK,
            create_time__year=now.year,
            create_time__month=now.month).order_by(
            '-visit_count')[:6]

        data = [{'id': item['blog_id'], 'title': tools.limit_str(item['blog__title']), 'pv': item['visit_count']} for
                item in res]

        return SucResponse(data=data)
