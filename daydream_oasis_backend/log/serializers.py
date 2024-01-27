# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/11/4 12:49
from rest_framework import serializers

from common.drf.serializers import DynamicFieldsSerializer


class ActionSerializer(DynamicFieldsSerializer):

    blog_id = serializers.IntegerField(help_text='博客id')
    action = serializers.IntegerField(help_text='行为')
    cost_time = serializers.FloatField(help_text='消耗的时长')

