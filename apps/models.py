#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:15
# @Author  : xuyiqing
# @File    : models.py
import math
from datetime import datetime

from bson.objectid import ObjectId
from django.db import models


class BaseManager(models.Manager):
    """objects对象操作方法"""

    def create(self, **kwargs):
        """
        对象创建，判无id
        :param kwargs:
        :return: obj
        """
        primary_id = kwargs.get("id")
        if not primary_id:
            primary_id = self.__gen_objectid()
        kwargs.update(dict(
            id=primary_id
        ))
        return super(BaseManager, self).create(**kwargs)

    def bulk_create(self, objs, **kwargs):
        """
        批量插入，判无id
        :param objs: model对象列表
        :param kwargs: 插入参数
        :return: objs
        """
        for obj in objs:
            if not obj.id:
                obj.id = self.__gen_objectid()
        return super(BaseManager, self).bulk_create(objs, **kwargs)

    @staticmethod
    def __gen_objectid():
        """
        生成分布式唯一ID，采用MongoDB的ObjectID
        :return: uuid
        """
        return str(ObjectId())

    @staticmethod
    def count_page(length: int, query_params) -> tuple:
        """
        分页获取页码
        :param length: queryset.count()
        :param query_params: url参数
        :return: tuple
        """
        page = int(query_params.get("page") or 1)
        page_size = int(query_params.get("page_size") or 10)
        pager = {
            "page_size": page_size,
            "max_page": int(math.ceil(length / page_size)),
            "page": page,
            "total": length,
        }
        return page, page_size, pager


class SourceBaseModel(models.Model):
    """models初始类，ID字段"""

    id = models.CharField(verbose_name="ID", primary_key=True, max_length=30)

    def save(self, **kwargs):
        """
        重写save，判无id
        :param kwargs:
        :return:
        """
        if not hasattr(self, "id") or not self.id:
            self.id = str(ObjectId())
        return super().save(**kwargs)

    class Meta:
        abstract = True


class BaseModel(SourceBaseModel):
    """models基类"""

    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    delete_time = models.DateTimeField(verbose_name="删除时间", null=True, default=None)

    objects = BaseManager()

    class Meta:
        abstract = True
