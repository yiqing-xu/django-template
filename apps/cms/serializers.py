#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 09:24
# @Author  : xuyiqing
# @File    : serializers.py
from serializers import BaseSerializer, serializers

from cms.models import FileModel


class FileSerializer(BaseSerializer):

    name = serializers.CharField(required=False)
    url = serializers.URLField(source='file.url', required=False)
    file = serializers.FileField(write_only=True)

    class Meta:
        model = FileModel
        fields = ['id', 'name', 'file', 'url']

    def validate(self, attrs):
        attrs.update(name=getattr(attrs.get('file'), 'name', 'file'))
        return attrs
