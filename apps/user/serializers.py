#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 22:19
# @Author  : xuyiqing
# @File    : serializers.py
from django.contrib.auth.hashers import make_password

from user.models import Account
from serializers import BaseSerializer


class AccountSerializer(BaseSerializer):

    class Meta:
        model = Account
        fields = ['id', 'name', 'username']
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.pop('password'))
        return super().create(validated_data)
