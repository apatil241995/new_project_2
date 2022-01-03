
from django.urls import path
from . import views

urlpatterns = [
    path('page/S_signup/', views.signup, name='S_signup'),
    path('page/S_login/', views.Login, name='S_login'),
    path('S_logout/', views.Logout, name='S_logout'),
    path("page/", views.s_login_page, name="s_login_page"),
    path("order_details/", views.GetPostListOfOrder),
    path("order_details/order/", views.OrderDetails),
    path('order_details/order/reject/', views.Reject)

]