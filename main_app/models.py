from django.db import models
from django.shortcuts import redirect


# Create your models here.


class Item(models.Model):
    description = models.TextField(max_length=75)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return redirect('item_list')
