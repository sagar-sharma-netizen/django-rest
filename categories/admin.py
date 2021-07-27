from django.contrib import admin
from django.conf import settings
from .models import (Category, SubCategory, Product)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "details"
    )
    search_fields = ("name",)
    list_filter = ("is_active", "is_deleted", "created_at", "modified_at", "name")
    readonly_fields = ()
    list_per_page = settings.DEFAULT_PAGE_SIZE
    raw_id_fields = ()

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "details",
        "category_id"
    )
    search_fields = ("name",)
    list_filter = ("is_active", "is_deleted", "created_at", "modified_at", "name")
    readonly_fields = ()
    list_per_page = settings.DEFAULT_PAGE_SIZE
    raw_id_fields = ("category_id",)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "details",
        "sub_category_id"
    )
    search_fields = ("name",)
    list_filter = ("is_active", "is_deleted", "created_at", "modified_at", "name")
    readonly_fields = ()
    list_per_page = settings.DEFAULT_PAGE_SIZE
    raw_id_fields = ("sub_category_id",)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
