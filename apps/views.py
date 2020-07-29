#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:15
# @Author  : xuyiqing
# @File    : views.py
from django.utils.decorators import method_decorator
from django.db import transaction
from rest_framework.views import APIView as BaseAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from response import JSONResponse


@method_decorator(transaction.atomic, name="dispatch")
class APIView(BaseAPIView):
    """视图基类"""
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        """
        接口分发
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.path.endswith('register') or request.method == 'GET':
            self.permission_classes.clear()
        response = super(APIView, self).dispatch(request, *args, **kwargs)
        if response.status_code != 200 and response.content_type != "application/json":
            return JSONResponse.noauth(response.data)
        return response
