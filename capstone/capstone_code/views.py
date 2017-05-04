from django.shortcuts import render, redirect
from capstone_code.models import Wine, Winery, Cellar
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from capstone_code.forms import SignUpForm



# Create your views here.


def render_winery_form(request):
    """
    
    :param request: 
    :return: 
    """

    return render(request, "./winery_form.html")

def render_profile(request):
    """
    
    :param request: 
    :return: 
    """
    user_name = User.first_name
    return render(request, "./home.html")


def render_wine_form(request):
    """
    
    :param request: 
    :return: 
    """
    return render(request, "./add_wine.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def view_wines(request):
    """
    
    :param request: 
    :return: 
    """

    return render(request, "./view_wines.html")


def view_winery(request):
    """
    
    :param request: 
    :return: 
    """

    return render(request, "./view_winery.html")

def home_page (request, username):

    user = User.objects.get(username=username)
    template = get_template('home.html')
    variables = Context({'username':username,})
    output = template.render(variable)
    return render(output)