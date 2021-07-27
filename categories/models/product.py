from __future__ import unicode_literals

from django.db import models
from categories.models import TimeStampable, SubCategory
from categories.managers.product import ProductManager, ProductQueryset


class Product(TimeStampable):
    """
    Product Model
    """
    name = models.CharField(
        verbose_name="Product Name",
        db_index=True,
        max_length=256
    )
    details = models.CharField(
        verbose_name="Product Details",
        blank=True,
        max_length=256
    )
    sub_category = models.ForeignKey(
        verbose_name="Sub Category",
        to=SubCategory,
        related_name="product_subcategory",
        on_delete=models.CASCADE
    )
    objects = ProductManager.from_queryset(ProductQueryset)()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
