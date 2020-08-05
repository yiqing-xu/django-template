#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 11:00
# @Author  : xuyiqing
# @File    : flush_channels.py
from django.conf import settings
from django.core.management import BaseCommand
from django_redis import get_redis_connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        conn = get_redis_connection()
        conn.delete(settings.WEBSOCKET_CHANNELS)
