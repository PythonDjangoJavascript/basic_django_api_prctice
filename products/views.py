from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Manufacturer, Product


class ProductDetailView(DetailView):
    """create view for product detail"""

    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(ListView):
    """Create view for products list"""

    model = Product
    template_name = 'products/product_list.html'
