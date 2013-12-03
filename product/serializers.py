from django.forms import widgets
from rest_framework import serializers
from product.models import *

''' Example for django-rest-framework.
class ApiSerial(serializers.ModelSerializer):
    class Meta:
        model = Garment
        fields = ('id', 'entity', 'cloth_type', 'color', 'quantity', 'entity_type')
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.entity = attrs.get('entity', instance.entity)
            instance.cloth_type = attrs.get('cloth_type', instance.cloth_type)
            instance.color = attrs.get('color', instance.color)
            instance.quantity = attrs.get('quantity', instance.quantity)
            instance.entity_type = attrs.get('entity_type', instance.entity_type)
            return instance
        return Garment(**attrs) 
'''

class ProductDefinitionApi(serializers.ModelSerializer):
    class Meta:
        model = Product_Definition
        fields = ('id', 'product_name', 'primary_image', 'description')
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.product_name = attrs.get('product_name', instance.product_name)
            instance.product_image = attrs.get('product_image', instance.product_image)
            instance.description = attrs.get('description', instance.description)
            return instance
        return Product_Definition(**attrs)

        
