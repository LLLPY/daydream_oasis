from common.drf.response import SucResponse
from common.views import BaseViewSet
from log.models import Action
from log.serializers import ActionSerializer
from rest_framework.decorators import action


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
                    def wrapped(self, request, *args, **kwargs):
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


class ActionViewSet(BaseViewSet):

    serializer_class = ActionSerializer
    queryset = Action.objects.all()

    @action(methods=['post'], detail=True)
    def upload_action(self, request, *args, **kwargs):
        action_obj: Action = self.get_object(raise_on_not_found=True)
        serialzer = self.get_serializer(data=self.request.data, include_fields=['action', 'cost_time'])
        serialzer.is_valid(raise_exception=True)
        action = serialzer.data.get('action')
        cost_time = serialzer.data.get('cost_time')
        action_obj.action = action

        return SucResponse()
