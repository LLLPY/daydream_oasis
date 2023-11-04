# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/11/4 12:49
from common.drf.serializers import DynamicFieldsSerializer
from rest_framework import serializers


class ActionSerializer(DynamicFieldsSerializer):

    action = serializers.IntegerField(help_text='希望')
    cost_time = serializers.FloatField(help_text='消耗的时长')

