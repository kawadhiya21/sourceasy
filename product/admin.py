from django.contrib import admin
from product.models import *

class FabricConstants(admin.ModelAdmin):
    list_display = ('constant_type','constant_value',)
    list_filter = ('constant_type',)
admin.site.register(Fabric_Constants,FabricConstants)
admin.site.register(Product_Fabric)
