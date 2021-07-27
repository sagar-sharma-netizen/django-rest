from __future__ import unicode_literals

from django.db import models
from categories.models import TimeStampable, Category
from categories.managers.subcategory import SubCategoryManager, SubCategoryQueryset


class SubCategory(TimeStampable):
    """
    Sub Category Model
    """
    name = models.CharField(
        verbose_name="Sub Category Name",
        db_index=True,
        max_length=256
    )
    details = models.CharField(
        verbose_name="Sub Category Details",
        blank=True,
        max_length=256
    )
    category = models.ForeignKey(
        verbose_name="Category",
        to=Category,
        related_name="subcategory_category",
        on_delete=models.CASCADE
    )
    objects = SubCategoryManager.from_queryset(SubCategoryQueryset)()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
