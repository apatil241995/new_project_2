from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from order_menu import views
from order_menu import models
from customer.models import customer_login, Orderedfood
# Anish
@csrf_exempt
def home(request):
    if request.method == "POST":
        a = request.POST['username']
        customer = customer_login.objects.get(username=a)
        food_details = models.OrderMenu.objects.all()
        return render(request, "home.html", {"food_details": food_details, "c_name":customer.c_name})
    else:
        food_details = models.OrderMenu.objects.all()
        return render(request, "home.html", {"food_details": food_details})


# Anish
@csrf_exempt
def additem(request):
    item_details = request.POST
    name = list(item_details)[0]
    Orderedfood.objects.create(
        food_details=models.OrderMenu.objects.get(food_name=name)
    )
    return HttpResponseRedirect("/home/v1/")

