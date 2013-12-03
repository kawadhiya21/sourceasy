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
# django-rest framework imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from product.serializers import *
from customer_enquiry.models import *

def new(request):
    return render_to_response('customer_enquiry/new.html',{
        'product_definition' : Product_Definition.objects.all()    
    }, context_instance=RequestContext(request))
