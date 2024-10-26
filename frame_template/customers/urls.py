from django.urls import path
from .views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

app_name = "customers"

urlpatterns = [
    path("list/", CustomerListView.as_view(), name="customer-list"),
    path("create/", CustomerCreateView.as_view(), name="customer-create"),
    path("update/<int:pk>/", CustomerUpdateView.as_view(), name="customer-update"),
    path("delete/<int:pk>/", CustomerDeleteView.as_view(), name="customer-delete"),
    path("detail/<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
]
