from django.urls import path

from customer import views

urlpatterns = [
    path('order_details/', views.OrderedFoodPostDelete),
    path('order_details/<name>', views.OrderedFoodPostDelete),
    path('cart/', views.CartGetDelete),
    path('checkout/', views.checkout),
    path('c_login_page/C_signup/', views.signup, name='C_signup'),
    path('c_login_page/C_login/', views.Login, name='C_login'),
    path('c_login_page/C_logout/', views.Logout, name='C_logout'),
    path('c_login_page/', views.c_login_page)
]
