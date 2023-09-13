from rest_framework import serializers
from common.drf.serializers import DynamicFieldsSerializer
import re
from common.exception import exception
# 用户
class UserSerializers(DynamicFieldsSerializer):
    mobile = serializers.CharField(max_length=11, min_length=11, required=True, help_text='手机号码')
    code = serializers.CharField(required=True, help_text='验证码')


    def validate_mobile(self,value):
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

    # 更新


# 留言
class MessageSerializers(serializers.ModelSerializer):
    ...
