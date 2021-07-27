# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models


class ProductQueryset(models.QuerySet):
    def filter_is_deleted(self, is_deleted: bool):
        return self.filter(is_deleted=is_deleted)

    def filter_is_active(self, is_active: bool):
        return self.filter(is_active=is_active)

    def filter_by_sub_category(self, sub_category_id: int):
        return self.filter(sub_category_id=sub_category_id)

    def filter_by_category(self, category_id: int):
        return self.filter(sub_category__category_id=category_id)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self.db)
