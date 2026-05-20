from django.urls import path
from .views import product_list, category_product_list, product_detail

app_name= 'products'
urlpatterns = [
    path('',product_list,name="product_list"),
    path('category/<slug:slug>', category_product_list,name='category_products'),
    path(
        'product/<int:id>/<slug:slug>/',
        product_detail,
        name='product_detail'
    )

]