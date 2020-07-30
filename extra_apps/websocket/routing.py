# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 18:43
# @Author  : xuyiqing
# @File    : routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from websocket.urls import websocket_urlpatterns


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
