import json
from typing import Optional
from contextlib import suppress
from django.http import HttpResponse
from django.forms.models import model_to_dict
import utils.serializer
from utils.exception import CustomException
from utils.paginator import paginate_queryset
from categories.models import Category, SubCategory, Product


def index(request):
    categories = Category.objects.filter_is_active(is_active=True).filter_is_deleted(is_deleted=False)
    data = paginate_queryset(categories, page=1, page_size=10)
    data["results"] = utils.serializer.serialize(queryset=categories)
    return HttpResponse(
        json.dumps(data), status=200, content_type="application/json"
    )


def retrieve(request, pk):
    with suppress(Category.DoesNotExist):
        category = Category.objects.get(pk=pk)
        return HttpResponse(
            json.dumps(model_to_dict(category)), status=200, content_type="application/json"
        )
    body = CustomException(
        title="Item not found",
        invalid_params=[]
    ).as_dict()
    return HttpResponse(
        json.dumps(body), status=500, content_type="application/json"
    )


def get_subcategories(request, category_id: Optional[int] = None):
    sub_categories = SubCategory.objects.filter_is_active(is_active=True)
    if category_id:
        sub_categories = sub_categories.filter_by_category(category_id=category_id)
    data = paginate_queryset(sub_categories, page=1, page_size=10)
    data["results"] = utils.serializer.serialize(queryset=sub_categories)
    return HttpResponse(
        json.dumps(data), status=200, content_type="application/json"
    )


def get_create_products(request, category_id: Optional[int] = None, sub_category_id: Optional[int] = None, **kwargs):
    if request.method == "POST":
        return create_product(request, **kwargs)
    products = Product.objects.filter_is_active(is_active=True)
    if category_id:
        products = products.filter_by_category(category_id=category_id)
    if sub_category_id:
        products = products.filter_by_sub_category(sub_category_id=sub_category_id)
    data = paginate_queryset(products, page=1, page_size=10)
    data["results"] = utils.serializer.serialize(queryset=products)
    return HttpResponse(
        json.dumps(data), status=200, content_type="application/json"
    )


def create_product(request):
    body = request.body.decode('utf-8')
    print(body)
    content = json.loads(body) if body else {}
    if not content or not(content.get('name') and content.get('sub_category_id')):
        body = CustomException(
            title="Name and Subcategory are required!",
            invalid_params=[]
        ).as_dict()
        return HttpResponse(
            json.dumps(body), status=500, content_type="application/json"
        )

    # validate subcategory
    sub_category = None
    with suppress(SubCategory.DoesNotExist):
        sub_category = SubCategory.objects.get(pk=content.get("sub_category_id", 0))
    if not sub_category:
        body = CustomException(
            title="Sub Category not found",
            invalid_params=[]
        ).as_dict()
        return HttpResponse(
            json.dumps(body), status=500, content_type="application/json"
        )
    product = Product(
        name=content.get("name"),
        sub_category_id=content.get("sub_category_id"),
        details=content.get("detail", "")
    )
    product.save()
    return HttpResponse(
        json.dumps({"pk": product.pk}), status=201, content_type="application/json"
    )
