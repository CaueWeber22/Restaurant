from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food

#Show foods
def show_food(request):
    if request.method == 'GET':
        foods = Food.objects.all()  # Find all foods
    
    return render(request, 'show_food.html', {'foods':foods})


# Add food
@login_required(login_url='/user/login/')
def add_food(request):
    if request.method == "GET":  
            return render(request, 'add_food.html')
    
    # Post food
    elif request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('food_image')
        FoodCreate = Food.objects.create(
        name = name, price = price, category = category, image=image
        )
        FoodCreate.save
        return redirect('show_food')
    
# Main
def main (request):
     return render(request, 'main.html')

# Delete
@login_required(login_url='/user/login/')
def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect('show_food')  