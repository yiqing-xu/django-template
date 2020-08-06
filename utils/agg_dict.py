#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 14:04
# @Author  : xuyiqing
# @File    : agg_dict.py
import time


def time_consumer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)
    return wrapper


def agg_dict_keys(source_dict: dict) -> dict:
    dest_dict = {}
    for k, v in source_dict.items():
        if '__' in k:
            exter_key, inner_key = k.split("__")
            if exter_key not in dest_dict:
                dest_dict.update({exter_key: {inner_key: v}})
            else:
                dest_dict[exter_key].update({inner_key: v})
        else:
            dest_dict.update({k: v})
    return dest_dict


if __name__ == '__main__':
    source_d = dict(
        title='标题',
        content='内容',
        para__title='标题1',
        para__content='内容1',
        creator__id=1,
        creator__name='徐益庆',
        creator__dept_name='dan',
    )
    result = agg_dict_keys(source_d)
    print(result)
