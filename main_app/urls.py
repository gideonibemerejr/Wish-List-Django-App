from django.urls import path
from . import views


urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('add/', views.ItemCreate.as_view(), name='item_create'),
    path('delete/', views.ItemDelete.as_view(), name='item_delete'),
]
