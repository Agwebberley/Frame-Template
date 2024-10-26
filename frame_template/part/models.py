from django.db import models
from frame.models import BaseModel


class Part(BaseModel):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_quantity = models.IntegerField(null=True)

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Part",
            "list_title": "Parts",
            "create_title": "Create Part",
            "enable_search": True,
            "default_sort_by": "created_at",
            "list_url": "part-list",
            "navigation": True,
            "fields": [
                {
                    "name": "name",
                    "display_name": "Name",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "description",
                    "display_name": "Description",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "price",
                    "display_name": "Price",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "stock_quantity",
                    "display_name": "Stock Quantity",
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
                    {"name": "Create", "url": "part-create", "disabled": ["detail"]}
                ],
                "dropdown": [
                    {"name": "Details", "url": "part-detail", "disabled": ["detail"]},
                    {"name": "Edit", "url": "part-update"},
                    {"name": "Delete", "url": "part-delete"},
                ],
            },
        }
