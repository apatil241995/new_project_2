from django.db import models
from order_menu.models import OrderMenu

# Akshay
class customer_login(models.Model):
    c_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, primary_key=False)
    username = models.EmailField(max_length=20, primary_key=False, unique=True)
    mobile_no = models.IntegerField(unique=True)
    pass1 = models.CharField(max_length=20)
    pass2 = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.username

    empAuth_objects = models.Manager()

# Akshay
class customer_table(models.Model):
    username = models.EmailField()
    Table_no = models.IntegerField(null=True, blank=True)

# Anish
class Orderedfood(models.Model):
    food_details = models.ForeignKey(OrderMenu, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(customer_login, on_delete=models.CASCADE, null=True, default=1)
    ordered_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __int__(self):
        return self.food_details, self.customer_details

# Anish
class Cart(models.Model):
    food_name = models.CharField(max_length=50)
    food_price = models.IntegerField()
    food_count = models.IntegerField()
    food_image = models.ImageField(null=True)
