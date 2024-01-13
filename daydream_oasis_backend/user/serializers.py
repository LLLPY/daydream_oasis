from rest_framework import serializers
from common.drf.serializers import DynamicFieldsSerializer
import re
from common.exception import exception

from utils import tools


# 用户
class UserSerializers(DynamicFieldsSerializer):
    username = serializers.CharField(allow_blank=True, allow_null=True, help_text='用户名')
    mobile = serializers.CharField(allow_blank=True, max_length=11, min_length=11, allow_null=True,
                                   help_text='手机号码')
    code = serializers.CharField(required=True, help_text='验证码')
    password = serializers.CharField(required=True, help_text='密码')
    action = serializers.CharField(allow_null=True, help_text='操作')
    avatar = serializers.SerializerMethodField(help_text='头像')
    id = serializers.CharField(allow_blank=True, allow_null=True, help_text='')

    def validate_mobile(self, value):
        ...
        if not self.is_valid_mobile(value):
            raise exception.CustomValidationError('手机号码格式不正确!')
        # 监测手机号是否合法

    @classmethod
    def is_valid_mobile(cls, mobile: str) -> bool:
        return bool(re.match(r'^[1][345789][0-9]{9}$', mobile))

    # 监测验证码是否合法
    @classmethod
    def is_valid_code(cls, code):
        return bool(re.match(r'\d{4}', code))

    # 监测密码是否合法
    @classmethod
    def is_valid_password(cls, password):
        return bool(
            6 <= len(password) <= 20 and re.match(r'.*\d+.*', password) and re.match(r'.*[a-zA-Z]+.*', password))

    def get_avatar(self, obj):
        avatar = tools.get_full_media_url(obj.avatar)
        return avatar


# 留言
class MessageSerializers(serializers.ModelSerializer):
    ...
