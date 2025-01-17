from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show_food, name ="show_food"),
    path('add/', views.add_food, name="add_food"),
    path('delete_food/<int:food_id>/', views.delete_food, name='delete_food'),
]