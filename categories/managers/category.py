# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models


class CategoryQueryset(models.QuerySet):
    def filter_is_deleted(self, is_deleted: bool):
        return self.filter(is_deleted=is_deleted)

    def filter_is_active(self, is_active: bool):
        return self.filter(is_active=is_active)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQueryset(self.model, using=self._db)
