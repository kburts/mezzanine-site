from django.shortcuts import render
from django.views.generic import ListView

from .models import Item
# Create your views here.

class PortfolioListView(ListView):

    model = Item