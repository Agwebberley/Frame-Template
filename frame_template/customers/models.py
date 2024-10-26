from django.db import models
from frame.models import BaseModel


# Create your models here.
class Customer(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.TextField()

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Customer",
            "list_title": "Customers",
            "create_title": "Create Customer",
            "enable_search": True,
            "default_sort_by": "created_at",
            "list_url": "customer-list",
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
                    "name": "email",
                    "display_name": "Email",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "phone",
                    "display_name": "Phone",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "address",
                    "display_name": "Address",
                    "enable_in_list": False,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
            ],
            "actions": {
                "button": [
                    {
                        "name": "Create",
                        "url": "customer-create",
                        "disabled": ["detail"],
                    },
                ],
                "dropdown": [
                    {
                        "name": "Details",
                        "url": "customer-detail",
                        "disabled": ["detail"],
                    },
                    {
                        "name": "Edit",
                        "url": "customer-update",
                    },
                    {
                        "name": "Delete",
                        "url": "customer-delete",
                    },
                ],
            },
        }

    def __str__(self):
        return self.name
