from django.shortcuts import render
from frame.base_views import (
    BaseCreateView,
    BaseListView,
    BaseUpdateView,
    BaseDeleteView,
    BaseDetailView,
)
from .models import Part
from django.urls import reverse_lazy
# Create your views here.


class PartCreateView(BaseCreateView):
    model = Part


class PartListView(BaseListView):
    model = Part


class PartUpdateView(BaseUpdateView):
    model = Part
    success_url = reverse_lazy("parts-list")


class PartDeleteView(BaseDeleteView):
    model = Part
    success_url = reverse_lazy("parts-list")


class PartDetailView(BaseDetailView):
    model = Part
