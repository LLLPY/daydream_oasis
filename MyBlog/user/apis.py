from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import UserSerializers, MessageSerializers
from .models import User, Message
from common.apis import MyBaseViewSet


# 用户
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword', '')
        user_list = []
        for u in User.objects.filter(username__icontains=keyword):
            con = {
                'username': u.username,
                'avatar': u.avatar.url,
                'id': u.id
            }
            user_list.append(con)
        return JsonResponse({
            'code': '200',
            'msg': '响应成功!',
            'data': {
                'user_list': user_list[:10]
            }
        })


# 留言
class MessageViewSet(MyBaseViewSet):
    serializer_class = MessageSerializers
    queryset = Message.objects.all()
