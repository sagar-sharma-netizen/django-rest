from __future__ import unicode_literals


from django.db import models
from categories.models.timestampable import TimeStampable
from categories.managers.category import CategoryManager, CategoryQueryset


class Category(TimeStampable):
    """
    Category Model
    """
    name = models.CharField(
        verbose_name="Category Name",
        db_index=True,
        max_length=256,
        unique=True
    )
    details = models.CharField(
        verbose_name="Category Details",
        blank=True,
        max_length=256
    )
    objects = CategoryManager.from_queryset(CategoryQueryset)()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
