from django.contrib import admin
from .models import Food
from .models import Category

admin.site.register(Food)
admin.site.register(Category)