#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 13:41
# @Author  : xuyiqing
# @File    : emit.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django_redis import get_redis_connection


# 指定发送
def emit_msg(user_id=None, message=None):
    conn = get_redis_connection()
    channel_name = conn.hget(settings.WEBSOCKET_CHANNELS, user_id)
    if not channel_name:
        return
    else:
        channel_name = channel_name.decode()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(
        channel_name,
        {
            "type": "emit.msg",
            "data": dict(
                code=200,
                mag='发送成功',
                data=message
            )
        }
    )


# 消息群发
def mass_msg(user_ids: list, message=None):
    if not user_ids:
        return
    conn = get_redis_connection()
    channel_names = conn.hmget(settings.WEBSOCKET_CHANNELS, user_ids)
    channel_names = [ch.decode() for ch in channel_names if ch]
    channel_layer = get_channel_layer()
    if channel_names:
        # select_room_name = 'room.' + user_ids[0]
        select_room_name = async_to_sync(channel_layer.new_channel)(prefix='room.')
        for channel_name in channel_names:
            async_to_sync(channel_layer.group_add)(
                select_room_name,
                channel_name
            )
        async_to_sync(channel_layer.group_send)(
            select_room_name,
            {
                "type": "emit.msg",
                "data": dict(
                    code=200,
                    mag='发送成功',
                    data=message
                )
            }
        )
        async_to_sync(channel_layer.flush)()
        # for channel_name in channel_names:
        #     async_to_sync(channel_layer.group_discard)(
        #         select_room_name,
        #         channel_name
        #     )
