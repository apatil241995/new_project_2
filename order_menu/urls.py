from django.urls import path

from order_menu import views

urlpatterns = [
    path('home/', views.OrderMenuGetPost),
    path('<name>', views.OrderMenuGetPost),
    path('category/', views.CategoryGetPost),
    path('category/<name>', views.CategoryGetPost),
    path('sortbycategory/<name>', views.SortByCategory)
]