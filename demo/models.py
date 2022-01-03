from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    contact = models.CharField(max_length=50, null=True)
