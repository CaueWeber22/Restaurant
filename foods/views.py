from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food
from .models import Category
import os
from django.conf import settings

#Show foods
def show_food(request):
    if request.method == 'GET':
        foods = Food.objects.filter(is_available=True)
        
        categories = Category.objects.all() #Find all categories
    
        return render(request, 'show_food.html', {'foods': foods, 'categories': categories})


# Add food
@login_required(login_url='/user/login/')
def add_food(request):
    if request.method == "GET":  
            categories = Category.objects.all() #Find all categories

            return render(request, 'add_food.html', {'categories':categories})
    
    # Post food
    elif request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category_id')
        image = request.FILES.get('food_image')
        description = request.POST.get('description')

        FoodCreate = Food.objects.create(
                name=name,
                price=price,
                category_id=category_id,
                image=image,
                description=description
            )
        FoodCreate.save()
        return redirect('foods:show_food')
    
# Main
def home (request):
     return render(request, 'main.html')

# Delete
@login_required(login_url='/user/login/')
def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    #Delete image
    if food.image:
        image_path = os.path.join(settings.MEDIA_ROOT, str(food.image))
        
        if os.path.isfile(image_path):
            os.remove(image_path)

    food.delete()
    return redirect('foods:show_food')  

#Serch for foods
def food_search(request):
    category_id = request.GET.get('category')
    name = request.GET.get('name').strip()

    # Check if has filters
    if category_id or name:  
        filters = {"is_available": True}  # Dictionary for filters

        if category_id:  
            filters["category_id"] = category_id  
        
        if name:  
            filters["name__icontains"] = name 

        foods = Food.objects.filter(**filters)  # Searching
        
    else:  
        return redirect('foods:show_food')
        
    categories = Category.objects.all() #Find all categories
    
    return render(request, 'show_food.html', {"foods": foods, "categories": categories} )


