from django.db import models

# Anish
class Category(models.Model):
    category_name = models.CharField(unique=True, primary_key=True, max_length=50)
    id = models.IntegerField(unique=True)

# Anish
class OrderMenu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    food_name = models.CharField(max_length=50)
    food_price = models.IntegerField()
    food_image = models.ImageField(null=True)
