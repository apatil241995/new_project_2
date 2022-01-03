from django.db import models


# Akshay
class staff_login(models.Model):
    s_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, primary_key=False, null=True)
    username = models.EmailField(max_length=20, primary_key=False, unique=True)
    mobile_no = models.IntegerField(unique=True)
    pass1 = models.CharField(max_length=20)
    pass2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    empAuth_objects = models.Manager()


# Anish
class OrderDetailList(models.Model):
    food_name = models.CharField(max_length=50)
    food_number = models.IntegerField()
    customer_id = models.IntegerField(null=True)
