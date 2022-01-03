from django.shortcuts import render, redirect

from order_menu.models import OrderMenu
from django.contrib import messages
from django.contrib.auth import logout
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Akshay
@csrf_exempt
def signup(request):
    email = request.POST['email']
    c_name = request.POST['c_name']
    mobile_no = request.POST['mobile_no']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    if pass1 == pass2:
        user = models.customer_login.empAuth_objects.create(
            username=email,
            email=email,
            c_name=c_name,
            pass1=pass1,
            mobile_no=mobile_no
        )
        user.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/home/v1/customer/v1/c_login_page/')
    return HttpResponseRedirect('Passwords are not matching..', status=400)

# Akshay
@csrf_exempt
def c_login_page(request):
    if request.method == "GET":
        return render(request, "loginre.html")

# Akshay
@csrf_exempt
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        Table_no = request.POST["Table_no"]

        try:
            user = models.customer_login.empAuth_objects.get(username=username, pass1=pass1)

            if user is not None:
                models.customer_table.objects.create(username=username, Table_no=Table_no)
                return redirect('http://127.0.0.1:8000/home/v1/', {"c_name":username})
            else:
                messages.error(request, 'Bad Credentials')
        except Exception as identifier:
            return HttpResponseRedirect('Wrong Username Or Password', status=400)

# Akshay
@csrf_exempt
def Logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse('Logout..')

# Anish
@csrf_exempt
def OrderedFoodPostDelete(request, name=None):
    if request.method == 'POST':
        food_name = request.POST.get(food_name=name)
        customer_name = request.POST.get('customer_name')
        models.Orderedfood.objects.create(
            customer_details=models.customer_login.objects.get(first_name=customer_name),
            food_details=models.OrderMenu.objects.get(food_name=food_name),
        )
        return JsonResponse({"Data": "saved"})

    elif request.method == "DELETE":
        food_item_details = models.OrderMenu.objects.get(food_name=name)
        food_id = food_item_details.id
        remove_food_item = models.Orderedfood.objects.filter(food_details_id=food_id).first()
        remove_food_item.delete()
        return JsonResponse({'item': 'deleted'})

# Anish
@csrf_exempt
def CartGetDelete(request, name=None):
    if request.method == 'GET':
        cart_item = models.Cart.objects.all()
        cart_item.delete()
        id = list(request.GET)[0]
        food_details = models.Orderedfood.objects.filter(customer_details_id=id)
        customer_name = []
        food_name = []
        for data in food_details:
            customer_details = models.customer_login.objects.get(id=data.customer_details_id)
            food_details = models.OrderMenu.objects.get(id=data.food_details_id)
            x = customer_details.c_name
            y = food_details.food_name
            customer_name.append(x)
            food_name.append(y)
        food_count = {}
        for i in food_name:
            m = {f"{i}": food_name.count(i)}
            food_count.update(m)
        item_details_price = {}
        for keys, values in food_count.items():
            food = models.OrderMenu.objects.get(food_name=keys)
            price = {f"{keys}": values * food.food_price}
            item_details_price.update(price)

        for keys, values in item_details_price.items():
            data = models.OrderMenu.objects.get(food_name=keys)
            food = data.food_image
            models.Cart.objects.create(
                food_name=keys,
                food_price=values,
                food_count=food_count[keys],
                food_image=food
            )
        item_details = models.Cart.objects.all()
        return render(request, "kart.html", {"item_details": item_details})

    elif request.method == "POST":
        id = list(request.POST)[0]
        # print(id)
        food_item_details = OrderMenu.objects.get(food_name=id)
        food_id = food_item_details.id
        remove_food_item = models.Orderedfood.objects.filter(food_details_id=food_id)
        cart_item = models.Cart.objects.filter(food_name=id)
        cart_item.delete()
        remove_food_item.delete()
        item_details = models.Cart.objects.all()
        return render(request, "kart.html", {"item_details": item_details})

# Anish
@csrf_exempt
def checkout(request):
    id = list(request.POST)[0]
    food_details = models.Orderedfood.objects.filter(customer_details_id=id)
    data = models.Cart.objects.all()
    food_details.delete()
    data.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/home/v1/')
# Anish
@csrf_exempt
def profile(request):
    pass
