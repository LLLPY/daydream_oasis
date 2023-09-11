from rest_framework import serializers
from common.drf.serializers import DynamicFieldsSerializer


# 用户
class UserSerializers(DynamicFieldsSerializer):
    mobile = serializers.CharField(max_length=11, min_length=11, required=True, help_text='手机号码')
    code = serializers.CharField(required=True, help_text='验证码')


# 留言
class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
