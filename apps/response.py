#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:15
# @Author  : xuyiqing
# @File    : response.py
from typing import Union

from django.http import JsonResponse


class JSONResponse(object):
    """接口返回体"""
    success_code = 200
    badrequest_code = 400
    noauth_code = 401
    nopermission_code = 403
    notfound_code = 404
    servererr_code = 500

    @classmethod
    def success(cls, data: Union[list, dict] = None, pager: dict = None) -> JsonResponse:
        """
        200成功
        :param data: 数据结构体
        :param pager: 分页
        :return: JsonResponse
        """
        result: dict = dict(
            code=cls.success_code,
            msg="返回成功",
        )
        if data:
            result.update(data=data)
        if pager:
            result.update(pager=pager)
        return JsonResponse(result)

    @classmethod
    def badrequest(cls, msg: str) -> JsonResponse:
        """
        400错误请求
        :param msg: 错误信息
        :return: JsonResponse
        """
        result: dict = dict(
            code=cls.badrequest_code,
            msg=msg
        )
        return JsonResponse(result)

    @classmethod
    def noauth(cls, msg: str) -> JsonResponse:
        """
        401未登录认证
        :param msg: 错误信息
        :return: JsonResponse
        """
        result: dict = dict(
            code=cls.noauth_code,
            msg=msg
        )
        return JsonResponse(result)

    @classmethod
    def nopermission(cls, msg: str) -> JsonResponse:
        """
        403权限认证不足
        :param msg: 错误信息
        :return: JsonResponse
        """
        result: dict = dict(
            code=cls.nopermission_code,
            msg=msg
        )
        return JsonResponse(result)

    @classmethod
    def notfound(cls, msg: str) -> JsonResponse:
        """
        404资源不存在
        :param msg: 错误信息
        :return: JsonResponse
        """
        result: dict = dict(
            code=cls.notfound_code,
            msg=msg
        )
        return JsonResponse(result)

    @classmethod
    def servererr(cls, msg: str) -> JsonResponse:
        """
        500服务器错误
        :param msg: 错误信息(中间件异常捕获栈)
        :return: JsonResponse
        """
        result: dict = dict(
            code=cls.servererr_code,
            msg=msg
        )
        return JsonResponse(result)
