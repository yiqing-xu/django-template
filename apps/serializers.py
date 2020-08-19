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
