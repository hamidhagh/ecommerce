from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store.as_view(), name='store'),
    path('search/product/', views.SearchProduct.as_view(), name="search_product"),
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    path('ascending_price/', views.ascending_price, name='ascending-price'),

]