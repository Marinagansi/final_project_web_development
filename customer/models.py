from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    customer_name=models.CharField(max_length=200)
    customer_email=models.CharField(max_length=200)
    customer_address=models.CharField(max_length=200)
    customer_password=models.CharField(max_length=200)
    
    class Meta:
        db_table="customer"