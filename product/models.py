from django.db import models
from product.models import *
from django.contrib.auth.models import User
from django.conf import settings
from product import constants as C
# Create your models here.

class Product_Definition(models.Model):
    user = models.ForeignKey(User)
    product_name = models.CharField(max_length=45,blank=False,default=False)
    primary_image = models.ImageField(upload_to="product_primary_image",blank=False,default=False)
    user_role = models.CharField(max_length=20,blank=False,default="admin")
    description = models.CharField(max_length=100,blank=True)

class Product_Definition_Secondary_Images(models.Model):
    product_definition = models.ForeignKey(Product_Definition)
    secondary_image = models.ImageField(upload_to="product_secondary_image",blank=False,default=False)

class Product_Sizes(models.Model):
    product_definition = models.ForeignKey(Product_Definition)
    size_name = models.CharField(max_length=5,blank=False,default=False)
    
class Product_Attribute(models.Model):
    product_definition = models.ForeignKey(Product_Definition)
    point_of_measurement = models.CharField(max_length=45,blank=False,default=False)

class Product_Attribute_Defaults(models.Model):
    product_attribute = models.ForeignKey(Product_Attribute, related_name="product_attribute")
    product_sizes = models.ForeignKey(Product_Sizes, related_name="product_sizes")
    default_value = models.CharField(max_length=10)

class Fabric_Constants(models.Model):
    constant_type = models.CharField(max_length=45,blank=False,default="fiber")
    constant_value = models.CharField(max_length=45,blank=False,default=None)
    
class Product_Fabric(models.Model):
    product_definition = models.ForeignKey(Product_Definition)
    fabric_type = models.CharField(max_length=30,choices=C.FABRIC_TYPE)
    fiber_one_name = models.ForeignKey(Fabric_Constants, related_name="fiber_one", blank=True, null=True, default=None)
    fiber_one_percentage = models.FloatField(blank=True)
    fiber_two_name = models.ForeignKey(Fabric_Constants, related_name="fiber_two", blank=True, null=True, default=None)
    fiber_two_percentage = models.FloatField(blank=True)
    fiber_three_name = models.ForeignKey(Fabric_Constants, related_name="fiber_three", blank=True, null=True, default=None)
    fiber_three_percentage = models.FloatField(blank=True)
    fiber_four_name = models.ForeignKey(Fabric_Constants, related_name="fiber_four", blank=True, null=True, default=None)
    fiber_four_percentage = models.FloatField(blank=True)
    lycra_percentage = models.FloatField(blank=True)
    construction_type = models.CharField(max_length=30,choices=C.CONSTRUCTION_TYPE)
    construction_name = models.ForeignKey(Fabric_Constants, related_name="construction_name", blank=True, null=True, default=None)
    fabric_gsm = models.IntegerField(blank=False)
