from django.contrib import admin
from .models import Comment, Food, FoodType

# Register your models here.

admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Comment)
