from django.shortcuts import render
from frame.base_views import (
    BaseCreateView,
    BaseListView,
    BaseUpdateView,
    BaseDeleteView,
    BaseDetailView,
)
from .models import Order, OrderItem
from django.urls import reverse_lazy
# Create your views here.


class OrderCreateView(BaseCreateView):
    model = Order
    success_url = reverse_lazy("order-list")


class OrderListView(BaseListView):
    model = Order


class OrderUpdateView(BaseUpdateView):
    model = Order
    success_url = reverse_lazy("order-list")

    def get_absolute_url(self):
        return reverse_lazy("order-list")


class OrderDeleteView(BaseDeleteView):
    model = Order
    success_url = reverse_lazy("order-list")

    def get_absolute_url(self):
        return reverse_lazy("order-list")


class OrderDetailView(BaseDetailView):
    model = Order


class OrderItemCreateView(BaseCreateView):
    model = OrderItem

    def get_absolute_url(self):
        return reverse_lazy("order-list")


class OrderItemListView(BaseListView):
    model = OrderItem


class OrderItemUpdateView(BaseUpdateView):
    model = OrderItem
    success_url = reverse_lazy("order-list")

    def get_absolute_url(self):
        return reverse_lazy("order-list")


class OrderItemDeleteView(BaseDeleteView):
    model = OrderItem
    success_url = reverse_lazy("orders-list")

    def get_absolute_url(self):
        return reverse_lazy("order-list")


class OrderItemDetailView(BaseDetailView):
    model = OrderItem
