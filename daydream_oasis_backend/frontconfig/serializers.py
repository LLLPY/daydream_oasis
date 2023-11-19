from common.drf.serializers import DynamicFieldsSerializer
from rest_framework import serializers


class FrontConfigSerializers(DynamicFieldsSerializer):
    format = serializers.CharField()
