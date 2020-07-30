#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 13:40
# @Author  : xuyiqing
# @File    : jobs.py
from typing import Union

from django_rq import job

from websocket.emit import emit_msg, mass_msg


@job
def send_message(user_id: str, data: Union[dict, list]):
    emit_msg(user_id, data)


@job
def mass_message(user_id: list, data: Union[dict, list]):
    mass_msg(user_id, data)
