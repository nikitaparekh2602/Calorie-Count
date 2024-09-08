from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Consume

def index(request):
    if request.method == 'POST':
        food_consumed_id = request.POST.get('food_consumed')  # Fetch food ID from form
        
        if food_consumed_id:
            food_consumed = get_object_or_404(Food, id=food_consumed_id)  # Safely get Food by ID
            user = request.user
            consume = Consume(user=user, food_consumed=food_consumed)
            consume.save()

    # Fetch all food items and consumed foods
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    
    return render(request, 'calariecount/index.html', {'foods': foods, 'consumed_food': consumed_food})

def delete_food(request, id):
    consumed_food = get_object_or_404(Consume, id=id, user=request.user)
    consumed_food.delete()
    return redirect('index')