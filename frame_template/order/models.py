from django.db import models
from frame.models import BaseModel


class Order(BaseModel):
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=255, null=True)

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Order",
            "list_title": "Orders",
            "create_title": "Create Order",
            "enable_search": True,
            "default_sort_by": "created_at",
            "list_url": "order-list",
            "navigation": True,
            "fields": [
                {
                    "name": "customer",
                    "display_name": "Customer",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "order_date",
                    "display_name": "Order Date",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "total_amount",
                    "display_name": "Total Amount",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "status",
                    "display_name": "Status",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "created_at",
                    "display_name": "Created At",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": False,
                },
                {
                    "name": "updated_at",
                    "display_name": "Updated At",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": False,
                },
            ],
            "actions": {
                "button": [
                    {"name": "Create", "url": "order-create", "disabled": ["detail"]}
                ],
                "dropdown": [
                    {"name": "Details", "url": "order-detail", "disabled": ["detail"]},
                    {"name": "Edit", "url": "order-update"},
                    {"name": "Delete", "url": "order-delete"},
                ],
            },
        }


class OrderItem(BaseModel):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    part = models.ForeignKey("part.Part", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    @classmethod
    def get_config(cls):
        return {
            "model_name": "OrderItem",
            "list_title": "OrderItems",
            "create_title": "Create OrderItem",
            "enable_search": True,
            "default_sort_by": "created_at",
            "list_url": "orderitem-list",
            "navigation": True,
            "fields": [
                {
                    "name": "order",
                    "display_name": "Order",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "part",
                    "display_name": "Part",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "quantity",
                    "display_name": "Quantity",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "unit_price",
                    "display_name": "Unit Price",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "created_at",
                    "display_name": "Created At",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "updated_at",
                    "display_name": "Updated At",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
            ],
            "actions": {
                "button": [
                    {
                        "name": "Create",
                        "url": "orderitem-create",
                        "disabled": ["detail"],
                    }
                ],
                "dropdown": [
                    {
                        "name": "Details",
                        "url": "orderitem-detail",
                        "disabled": ["detail"],
                    },
                    {"name": "Edit", "url": "orderitem-update"},
                    {"name": "Delete", "url": "orderitem-delete"},
                ],
            },
        }
