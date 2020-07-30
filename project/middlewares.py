#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 20:19
# @Author  : xuyiqing
# @File    : middlewares.py
import logging
import traceback

from django.conf import settings
from django.middleware.common import MiddlewareMixin

from response import JSONResponse


class CSRFIgorneMiddleware(MiddlewareMixin):
    """去除csrf验证"""

    @staticmethod
    def process_request(request):
        setattr(request, '_dont_enforce_csrf_checks', True)


class ExceptionHandlerMiddleware(MiddlewareMixin):
    """异常处理"""

    @staticmethod
    def process_exception(request, exception):
        logger = logging.getLogger("api")
        info = traceback.format_exc()
        logger.error(info)
        if not settings.RETURN_ERR_INFO:
            info = "系统报错"
        return JSONResponse.servererr(info)
