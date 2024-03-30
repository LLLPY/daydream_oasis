from rest_framework import serializers

from common.drf.serializers import DynamicFieldsSerializer


class FrontConfigSerializers(DynamicFieldsSerializer):
    format = serializers.CharField()
