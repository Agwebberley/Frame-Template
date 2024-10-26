from django.urls import path
from .views import (
    PartCreateView,
    PartListView,
    PartUpdateView,
    PartDeleteView,
    PartDetailView,
)

urlpatterns = [
    path("Part/create/", PartCreateView.as_view(), name="part-create"),
    path("Part/list/", PartListView.as_view(), name="part-list"),
    path("Part/update/<int:pk>/", PartUpdateView.as_view(), name="part-update"),
    path("Part/delete/<int:pk>/", PartDeleteView.as_view(), name="part-delete"),
    path("Part/detail/<int:pk>/", PartDetailView.as_view(), name="part-detail"),
]
