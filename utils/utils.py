#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 14:13
# @Author  : xuyiqing
# @File    : utils.py
from django.core.cache import cache


def cache_decorator(key: str, exp: int = 60 * 60 * 24):
    def wrapper(func):
        def handler(*args, **kwargs):
            value = cache.get(key)
            if value is None:
                value = func(*args, **kwargs)
                cache.set(key, value, exp)
            return value
        return handler
    return wrapper
