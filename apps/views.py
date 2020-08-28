#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:15
# @Author  : xuyiqing
# @File    : views.py
import logging

from django.utils.decorators import method_decorator
from django.db import transaction
from django.http import JsonResponse
from rest_framework.views import APIView as BaseAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from response import JSONResponse


@method_decorator(transaction.atomic, name="dispatch")
class APIView(BaseAPIView, JSONResponse):
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
        logger = logging.getLogger("api")
        if request.path.endswith('register') or request.method == 'GET':
            self.permission_classes.clear()
        result = super(APIView, self).dispatch(request, *args, **kwargs)
        logger.info("path-->{}, method-->{}, IP-->{}, user-->{}".format(
            request.path,
            request.method,
            request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get("REMOTE_ADDR"),
            request.user
        ))
        if isinstance(result, dict):
            return JsonResponse(result)
        else:
            if hasattr(result, "status_code"):
                if result.status_code != 200 and result.content_type != "application/json":
                    return self.noauth(result.data)
            return result
