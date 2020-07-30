#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 11:09
# @Author  : xuyiqing
# @File    : consumers.py
import logging
from urllib import parse

from django.conf import settings
from channels.generic.websocket import JsonWebsocketConsumer
from django_redis import get_redis_connection

from utils.jwt import jwt_decode_handler


class CustomJsonMessageConsumer(JsonWebsocketConsumer):
    """websocket连接"""

    def __init__(self, *args, **kwargs):
        self.channel_user: str = ''
        super().__init__(*args, **kwargs)

    def decode_query_params(self):
        return {k: v[0] for k, v in parse.parse_qs(self.scope['query_string'].decode()).items()}

    def connect(self):
        """
        连接触发
        :return:
        """
        logger = logging.getLogger('websocket')
        query_parms = self.decode_query_params()
        encode_bearer_token = query_parms.get("token")
        if not encode_bearer_token:
            self.disconnect(401)
        try:
            decode_bearer_token: dict = jwt_decode_handler(encode_bearer_token)
        except Exception as e:
            logger.error("解析token，{}".format(e.args))
            self.disconnect(400)
            return
        user_id: str = decode_bearer_token["user_id"]
        self.accept()
        self.channel_user = user_id
        conn = get_redis_connection()
        conn.hset(settings.WEBSOCKET_CHANNELS, user_id, self.channel_name)

    def disconnect(self, code):
        """
        断开连接触发
        :param code:
        :return:
        """
        conn = get_redis_connection()
        conn.hdel(settings.WEBSOCKET_CHANNELS, self.channel_user)

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        """
        收到消息触发
        :param text_data: 文本
        :param bytes_data: 字节
        :param kwargs:
        :return:
        """
        logger = logging.getLogger("websocket")
        logger.info(text_data)
        pass

    def emit_msg(self, event):
        self.send_json(event['data'])
