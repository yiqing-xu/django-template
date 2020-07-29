#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:15
# @Author  : xuyiqing
# @File    : auth.py
from user.models import Account
from user.serializers import AccountSerializer


def jwt_response_payload_handler(token, user: Account, request, *args):
    data = AccountSerializer(instance=user).data
    data.update(token=token)
    return data
