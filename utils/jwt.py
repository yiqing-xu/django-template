#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 11:11
# @Author  : xuyiqing
# @File    : jwt.py
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 生成token
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 解析token
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
