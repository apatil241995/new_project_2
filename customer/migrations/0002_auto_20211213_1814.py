# Generated by Django 3.0.3 on 2021-12-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_table',
            name='Table_no',
            field=models.IntegerField(null=True),
        ),
    ]
