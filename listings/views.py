from django.shortcuts import render, get_object_or_404
from .models import Category, Product
categories = Category.objects.all()
def product_list(request, category_slug=None):
    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)

    else:
        requested_category = None
        products = Product.objects.all()

    return render(
        request,
        'product/list.html',
        {
            'categories': categories,
            'requested_category': requested_category,
            'products': products
        }
    )

def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(
        Product,
        category_id = category.id,
        slug = product_slug
    )

    return render(
        request,
        'product/detail.html',
        {
            'product': product
        }
    )
# Create your views here.
