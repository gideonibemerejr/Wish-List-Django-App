from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import *


class ItemList(ListView):
    model = Item


class ItemCreate(CreateView):
    model = Item
    fields = 'description',


class ItemDelete(DeleteView):
    model = Item
