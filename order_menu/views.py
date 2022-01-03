from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from order_menu import models

# Anish
@csrf_exempt
def OrderMenuGetPost(request, name=None):
    if request.method == 'GET':
        if name is None:
            order_data = models.OrderMenu.objects.all()
            response = {}
            for data in order_data:
                food_item = {data.food_name: data.food_price}
                response.update(food_item)
            return JsonResponse(response)
        else:
            order_data = models.OrderMenu.objects.get(food_name=name)
            response = {f'{order_data.food_name}': f'{order_data.food_price}'}
            return JsonResponse(response)

    elif request.method == 'POST':
        name = request.POST.get('category_name')
        models.OrderMenu.objects.create(
            category=models.Category.objects.get(category_name=name),
            food_name=request.POST.get('food_name'),
            food_price=request.POST.get('food_price')
        )
        return JsonResponse({"Data": "saved"})

    elif request.method == "DELETE":
        food_item = models.OrderMenu.objects.get(food_name=name)
        food_item.delete()
        return JsonResponse({'data': 'deleted'})

# Anish
@csrf_exempt
def CategoryGetPost(request, name=None):
    if request.method == 'GET':
        category_data = models.Category.objects.all()
        response = {}
        for data in category_data:
            z = {data.id: data.category_name}
            response.update(z)
        return JsonResponse(response)

    elif request.method == 'POST':
        models.Category.objects.create(
            id=request.POST.get('id'),
            category_name=request.POST.get('category_name')
        )
        return JsonResponse({'msg': 'saved'})

    elif request.method == "DELETE":
        food_item = models.Category.objects.get(category_name=name)
        food_item.delete()
        return JsonResponse({'data': 'deleted'})

# Anish
@csrf_exempt
def SortByCategory(request, name):
    if request.method == "GET":
        food_items = models.OrderMenu.objects.filter(category=name)
        response = {}
        for data in food_items:
            x = {data.food_name: data.food_price}
            response.update(x)
        return JsonResponse(response)
