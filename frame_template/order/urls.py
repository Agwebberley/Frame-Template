from django.urls import path
from .views import (
    OrderCreateView,
    OrderListView,
    OrderUpdateView,
    OrderDeleteView,
    OrderDetailView,
    OrderItemCreateView,
    OrderItemListView,
    OrderItemUpdateView,
    OrderItemDeleteView,
    OrderItemDetailView,
)

urlpatterns = [
    path("Order/create/", OrderCreateView.as_view(), name="order-create"),
    path("Order/list/", OrderListView.as_view(), name="order-list"),
    path("Order/update/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
    path("Order/delete/<int:pk>/", OrderDeleteView.as_view(), name="order-delete"),
    path("Order/detail/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("OrderItem/create/", OrderItemCreateView.as_view(), name="orderitem-create"),
    path("OrderItem/list/", OrderItemListView.as_view(), name="orderitem-list"),
    path(
        "OrderItem/update/<int:pk>/",
        OrderItemUpdateView.as_view(),
        name="orderitem-update",
    ),
    path(
        "OrderItem/delete/<int:pk>/",
        OrderItemDeleteView.as_view(),
        name="orderitem-delete",
    ),
    path(
        "OrderItem/detail/<int:pk>/",
        OrderItemDetailView.as_view(),
        name="orderitem-detail",
    ),
]
