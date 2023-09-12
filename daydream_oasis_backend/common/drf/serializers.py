# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/9/8 23:11  

from rest_framework import serializers


# 参数校验时，动态指定
class DynamicFieldsSerializer(serializers.Serializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    参考：https://www.django-rest-framework.org/api-guide/serializers/#example
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        include_fields = kwargs.pop('include_fields', None)
        exclude_fields = kwargs.pop('exclude_fields', None)
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        # 指定的字段：如果设置了，需要检验的字段就是这些
        if include_fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(include_fields)  # 需要的
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        # 需要排除掉的字段：如果有很多字段需要校验，但是有一两个不需要，就可以使用exclude_fields来排除掉这些不需要校验的字段
        if exclude_fields is not None:
            for field_name in exclude_fields:
                self.fields.pop(field_name)

    class Meta:
        abstract = True
