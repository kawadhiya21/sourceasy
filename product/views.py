#python imports
from PIL import Image
# django imports
from django.utils.html import escape
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect , Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
# local imports
from product.utils import *
from product.models import *
from users.views import *
from product import constants as C

@login_required
@is_operator
def add(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        name = escape(request.POST['name'])
        primary_image = request.FILES['primary_image']
        print primary_image.content_type
        description = escape(request.POST['description'])
        #user_role to be defined. Right now its admin is pranay.
        product_definition = Product_Definition.objects.create(user=user,product_name=name,primary_image=primary_image,description=description)
        product_definition.save()
        secondary_image_count = int(request.POST['secondary_image_count'])
        if secondary_image_count > 0 :
            for num in range(1,secondary_image_count+1):
                try:
                    secondary_image = request.FILES['secondary_image_'+str(num)]
                    secondary_images = Product_Definition_Secondary_Images.objects.create(product_definition=product_definition,secondary_image=secondary_image)
                    secondary_images.save()
                except:
                    pass
        return redirect('/product/add_sizes/'+str(product_definition.id))        
    return render_to_response('product/add.html', context_instance=RequestContext(request))

@login_required
@is_operator
def add_sizes(request,product_id):
    user = User.objects.get(username=request.user)
    product_definition = Product_Definition.objects.get(pk=product_id)
    if request.method == 'POST':
        product_definition =  Product_Definition.objects.get(pk=product_id)
        size_list_num = int(escape(request.POST['size_list_num']))
        for num in range(1,size_list_num+1):
            try: 
                size = escape(request.POST['name_'+str(num)])
                if size:
                    product_size = Product_Sizes.objects.create(product_definition=product_definition,size_name=size)
                    product_size.save()
            except:
                pass
        return redirect('/product/add_size_details/'+str(product_definition.id))
    return render_to_response('product/add_sizes.html', { 'product_definition' : product_definition } ,context_instance=RequestContext(request))
    
@login_required
@is_operator
def add_size_details(request,product_id):
    user = User.objects.get(username=request.user)
    product_definition = Product_Definition.objects.get(pk=product_id)
    product_size = Product_Sizes.objects.filter(product_definition=product_definition)
    product_definition =  Product_Definition.objects.get(pk=product_id)
    if request.method == 'POST':
        detail_size_num = int(escape(request.POST['detail_size_num']))
        for num in range(1,detail_size_num+1):
            pa = escape(request.POST['pa'+str(num)])
            if pa != "":
                product_attribute = Product_Attribute.objects.create(product_definition=product_definition,point_of_measurement=pa)
                product_attribute.save()
                for atr in range(0,len(product_size)):
                    default_value = escape(request.POST[str(num)+'_'+str(product_size[atr].id)])
                    product_attribute_default = Product_Attribute_Defaults.objects.create(product_attribute=product_attribute,product_sizes=product_size[atr],default_value=default_value)
                    product_attribute_default.save()
            return redirect('/product/add_fabric/'+str(product_definition.id))          
    return render_to_response('product/add_size_details.html',{
        'product_definition' : product_definition,
        'product_size' : product_size
    }, context_instance=RequestContext(request))
    
@login_required
@is_operator
def add_fabric(request,product_id):
    message = ""
    product_definition = Product_Definition.objects.get(pk=product_id)
    if request.method  == "POST":
        try:
            basefiber1_type = escape(request.POST['basefiber1_type'])
            basefiber1_percentage = escape(request.POST['basefiber1_percentage'])
            basefiber1_type = Fabric_Constants.objects.get(constant_value = basefiber1_type)
        except:
            basefiber1_type = None
            basefiber1_percentage = 0
        try:
            basefiber2_type = escape(request.POST['basefiber2_type'])
            basefiber2_percentage = escape(request.POST['basefiber2_percentage'])
            basefiber2_type = Fabric_Constants.objects.get(constant_value = basefiber2_type)
        except:
            basefiber2_type = None
            basefiber2_percentage = 0
        try:
            basefiber3_type = escape(request.POST['basefiber3_type'])
            basefiber3_percentage = escape(request.POST['basefiber3_percentage'])
            basefiber3_type = Fabric_Constants.objects.get(constant_value = basefiber3_type)
        except:
            basefiber3_type = None
            basefiber3_percentage = 0
        try:
            basefiber4_type = escape(request.POST['basefiber4_type'])
            basefiber4_percentage = escape(request.POST['basefiber4_percentage'])
            basefiber4_type = Fabric_Constants.objects.get(constant_value = basefiber4_type)
        except:
            basefiber4_type = None
            basefiber4_percentage = 0
        try:
            lycra_percentage = escape(request.POST['baselycra'])
            lycra = Fabric_Constants.objects.get(constant_type = "lycra")
        except:
            lycra = Fabric_Constants.objects.get(constant_type = "lycra")
            lycra_percentage = 0    
        try:
            basegsm = escape(request.POST['basegsm'])
        except:
            basegsm = 0
        try:    
            baseconstruction_type_c = escape(request.POST['baseconstruction_type'])
            if baseconstruction_type_c == 'knitted':
                baseconstruction_type = C.CONSTRUCTION_TYPE[0]
            elif baseconstruction_type_c == 'woven':
                baseconstruction_type = C.CONSTRUCTION_TYPE[1]
            baseconstruction_name = escape(request.POST["base_"+str(baseconstruction_type_c)])
            baseconstruction_name = Fabric_Constants.objects.get(constant_value=baseconstruction_name)
        except:
            baseconstruction_type = C.CONSTRUCTION_TYPE[2]
            baseconstruction_name = Fabric_Constants.objects.get(constant_value="default")
        product_fabric = Product_Fabric(product_definition=product_definition,fabric_type=C.FABRIC_TYPE[0],
        fiber_one_name = basefiber1_type, fiber_one_percentage =basefiber1_percentage,
        fiber_two_name = basefiber2_type, fiber_two_percentage =basefiber2_percentage,
        fiber_three_name = basefiber3_type, fiber_three_percentage =basefiber3_percentage,
        fiber_four_name = basefiber4_type, fiber_four_percentage =basefiber4_percentage,
        lycra_percentage = lycra_percentage,
        fabric_gsm = basegsm, construction_type = baseconstruction_type, construction_name = baseconstruction_name)
        product_fabric.save()
        
        trim_fabric_count = int(escape(request.POST['trim_fabric_count']))
        for x in range(1,trim_fabric_count+1):
            ignore = escape(request.POST.get('trim'+str(x)+'ignore',False))
            if ignore == 'False':
                try:
                    trimfiber1_type = escape(request.POST['trim'+str(x)+'fiber1_type'])
                    trimfiber1_percentage = escape(request.POST['trim'+str(x)+'fiber1percentage'])
                    trimfiber1_type = Fabric_Constants.objects.get(constant_value = trimfiber1_type)
                except:
                    trimfiber1_type = None
                    trimfiber1_percentage = 0
                try:
                    trimfiber2_type = escape(request.POST['trim'+str(x)+'fiber2_type'])
                    trimfiber2_percentage = escape(request.POST['trim'+str(x)+'fiber2percentage'])
                    trimfiber2_type = Fabric_Constants.objects.get(constant_value = trimfiber2_type)
                except:
                    trimfiber2_type = None
                    trimfiber2_percentage = 0
                try:
                    trimfiber3_type = escape(request.POST['trim'+str(x)+'fiber3_type'])
                    trimfiber3_percentage = escape(request.POST['trim'+str(x)+'fiber3percentage'])
                    trimfiber3_type = Fabric_Constants.objects.get(constant_value = trimfiber3_type)
                except:
                    trimfiber3_type = None
                    trimfiber3_percentage = 0
                try:
                    trimfiber4_type = escape(request.POST['trim'+str(x)+'fiber4_type'])
                    trimfiber4_percentage = escape(request.POST['trim'+str(x)+'fiber4percentage'])
                    trimfiber4_type = Fabric_Constants.objects.get(constant_value = trimfiber4_type)
                except:
                    trimfiber4_type = None
                    trimfiber4_percentage = 0
                try:
                    lycra_percentage = escape(request.POST['trim'+str(x)+'lycra'])
                    lycra = Fabric_Constants.objects.get(constant_type = "lycra")
                except:
                    lycra = Fabric_Constants.objects.get(constant_type = "lycra")
                    lycra_percentage = 0
                try:
                    trimgsm = escape(request.POST['trim'+str(x)+'gsm'])
                except:
                    trimgsm = 0
                try:    
                    trimconstruction_type_c = escape(request.POST['trim'+str(x)+'construction_type'])
                    if trimconstruction_type_c == 'knitted':
                        trimconstruction_type = C.CONSTRUCTION_TYPE[0]
                    elif trimconstruction_type_c == 'woven':
                        trimconstruction_type = C.CONSTRUCTION_TYPE[1]
                        trimconstruction_name = escape(request.POST["trim"+str(x)+str(trimconstruction_type_c)])
                    trimconstruction_name = Fabric_Constants.objects.get(constant_value=baseconstruction_name)
                except:
                    trimconstruction_type = C.CONSTRUCTION_TYPE[2]
                    trimconstruction_name = Fabric_Constants.objects.get(constant_value="default")
                product_fabric = Product_Fabric(product_definition=product_definition,fabric_type=C.FABRIC_TYPE[1],
                fiber_one_name = trimfiber1_type, fiber_one_percentage =trimfiber1_percentage,
                fiber_two_name = trimfiber2_type, fiber_two_percentage =trimfiber2_percentage,
                fiber_three_name = trimfiber3_type, fiber_three_percentage =trimfiber3_percentage,
                fiber_four_name = trimfiber4_type, fiber_four_percentage =trimfiber4_percentage,
                lycra_percentage = lycra_percentage,
                fabric_gsm = trimgsm, construction_type = trimconstruction_type, construction_name = trimconstruction_name)
                product_fabric.save()
    fabric_constants = Fabric_Constants.objects.all()
    return render_to_response("product/add_fabric.html",{
        'fabric_constants' : fabric_constants,
        'message' : message,
    }, context_instance=RequestContext(request))

def test(request):
    return render_to_response("enquiry/create_enquiry.html", context_instance=RequestContext(request))
