from django.urls import path
from .views import order_create, order_confirmation, confirmed_orders, delete_order,edit_order

app_name = "orders"

urlpatterns = [
    path('create', order_create, name="order_create"),
    path("confirmation/<int:order_id>", order_confirmation, name="order_confirmation"),
    path("confirmed/", confirmed_orders, name="confirmed_orders"),
    path("delete/<int:order_id>/",delete_order, name="delete_order"),
    path('edit/<int:order_id>/',edit_order, name="edit_order"),  # Edit URL



]
