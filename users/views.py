from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect , Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
# Create your views here.
from users.utils import *

def is_admin(function):
    def wrapper(request, *args, **kw):
        user=request.user
        group = user.groups.all()[0].name
        if group != 'admin':
            return HttpResponseRedirect('/users/customer_demo')
        else:
            return function(request, *args, **kw)
    return wrapper

def is_operator(function):
    def wrapper(request, *args, **kw):
        user=request.user
        group = user.groups.all()[0].name
        if group != 'operators':
            return HttpResponseRedirect('/users/customer_demo')
        else:
            return function(request, *args, **kw)
    return wrapper    

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
	try:
	    user = User.objects.get(username=email)
	except User.DoesNotExist:
            user = create_user(email, password)
            g = Group.objects.get(name='customer') 
            g.user_set.add(user)
            message = "You have been registered successfully" 
            return render_to_response('users/index.html', {
                'message' : message,
            },context_instance=RequestContext(request))
	message = "The email already exists"
        return render_to_response('users/index.html', {
            'message' : message,
        },context_instance=RequestContext(request))

    return render_to_response('users/index.html', context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request,user)
            message = "Logged In"
        else:
            message = "Email/Password combination wrong"
        try:    
	        next_url = request.GET['next']
	        return HttpResponseRedirect(next_url)
        except:    
            return render_to_response('users/login.html', {
                'message' : message,
            },context_instance=RequestContext(request))
    return render_to_response('users/login.html', context_instance=RequestContext(request))

@login_required
@is_admin
def logged_in(request):
    return render_to_response('users/logged_in.html', context_instance=RequestContext(request))

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/users/login')

@login_required
def stub(request):
    return render_to_response('users/stub.html', context_instance=RequestContext(request))
