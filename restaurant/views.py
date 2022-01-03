from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render

from restaurant import models
from customer.models import customer_login, Orderedfood
from order_menu.models import OrderMenu
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


# Akshay
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        s_name = request.POST['s_name']
        mobile_no = request.POST['mobile_no']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            user = models.staff_login.empAuth_objects.create(username=email,
                                                             email=email,
                                                             s_name=s_name,
                                                             pass1=pass1,
                                                             mobile_no=mobile_no
                                                             )
            user.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/home/v1/restaurant/v1/page/")
        else:
            return HttpResponse('Passwords are not matching..', status=400)


# Akshay
@csrf_exempt
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        try:
            user = models.staff_login.empAuth_objects.get(username=username, pass1=pass1)
            if user is not None:
                return HttpResponseRedirect('/restaurant/v1/order_details/')
            else:
                messages.error(request, 'Bad Credentials')
        except Exception as identifier:
            return HttpResponse('Wrong Username Or Password', status=400)


# Akshay
@csrf_exempt
def Logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse('Logout..')


# Akshay
@csrf_exempt
def s_login_page(request):
    if request.method == "GET":
        return render(request, "staflogin.html")


# Anish
@csrf_exempt
def GetPostListOfOrder(request):
    if request.method == 'GET':
        list_of_order = Orderedfood.objects.all()
        response = []
        food_list = []
        for data in list_of_order:
            cus_details = customer_login.objects.get(email=data.customer_details)
            x = cus_details.c_name
            response.append(x)
        a = list(dict.fromkeys(response))
        b = {}
        for i in a:
            cus = customer_login.objects.get(c_name=i)
            id = cus.id
            food_details = Orderedfood.objects.filter(customer_details_id=id)
            b.update({f'{i}': food_details})
        return render(request, 'staffpage.html', {"c_name": a})


# Anish
@csrf_exempt
def OrderDetails(request):
    id = list(request.GET)[0]
    customer_id = customer_login.objects.get(c_name=id)
    food_details = Orderedfood.objects.filter(customer_details_id=customer_id.id)
    a = []
    for i in food_details:
        f_name = OrderMenu.objects.get(id=i.food_details_id)
        a.append(f_name.food_name)
    food = {}
    for j in a:
        c = a.count(j)
        food.update({f"{j}": c})

    return render(request, 'stafforder.html', {"order": food, "c_id": customer_id.id})


# Anish
@csrf_exempt
def Reject(request):
    id = list(request.POST)[0]
    food_detail = models.OrderDetailList.objects.filter(customer_id=id)
    food = Orderedfood.objects.filter(customer_details_id=id)
    food_detail.delete()
    food.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/restaurant/v1/order_details/')
