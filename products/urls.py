from django.urls import path
# from .views import ProductDetailView, ProductListView
from . import views

urlpatterns = [

    path('products/', views.product_list, name='product-list'),
    path('products/<int:id>', views.product_detail, name='product-detail'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer-list'),
    path('manufacturers/<int:id>', views.manufacturer_detail,
         name='manufacturer-detail'),
    # path('', ProductListView.as_view(), name="product-list"),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name="product-detail")
]
