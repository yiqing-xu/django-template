#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 22:22
# @Author  : xuyiqing
# @File    : serializers.py
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    对象序列化基类
    """
    id = serializers.CharField(required=False)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    def __init__(self, **kwargs):
        """
        去除冗余字段
        :param kwargs: (field1, field2, )
        """
        pop_fields: tuple = kwargs.pop("pop_fields", ())
        super(BaseSerializer, self).__init__(**kwargs)
        for field_name in pop_fields:
            self.fields.pop(field_name)


class ValidatorSerializer(serializers.Serializer):

    page = serializers.IntegerField(min_value=1, default=1, required=False,
                                    error_messages={"min_value": "页码最小设定为1"})
    page_size = serializers.IntegerField(min_value=1, max_value=100, default=10, required=False,
                                         error_messages={"min_value": "每页最少10条数据",
                                                         "max_value": "每页最多100条数据"})

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
