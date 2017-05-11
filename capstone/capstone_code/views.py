from django.shortcuts import render, redirect
from rest_framework import viewsets
from capstone_code.models import Wine, Winery, Cellar

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from capstone_code.forms import SignUpForm
from capstone_code.serializers import WineSerializer, WinerySerializer, CellarSerializer, UserSerializer, \
                                        GroupSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class WineViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, `destroy`, and `highlight` action.
    """

    # render_classes = [TemplateHTMLRenderer]
    # template_name = 'view_wines.html'
    serializer_class = WineSerializer
    queryset = Wine.objects.all()


    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)



class WineryViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows winery data to be viewed or edited
    """

    #render_classes = [TemplateHTMLRenderer]
    #template_name = 'view_winery.html'
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer



class CellarViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows personal cellar data to be viewed or edited
    """
    queryset = Cellar.objects.all()
    serializer_class = CellarSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


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
    user_data = User.objects.all()
    arguments = {'user': user_data}
    return render(request, "./home.html", arguments)


def render_wine_form(request):
    """
    
    :param request: 
    :return: 
    """
    return render(request, "./add_wine.html")

def render_cellar_form(request):
    """
    
    :param request: 
    :return: 
    """
    return render(request, "./add_cellar_data.html")


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
    all_wines = Wine.objects.all()
    arguments ={{'wine':all_wines}}
    return render(request, "./view_wines.html", arguments)


def view_winery(request):
    """
    
    :param request: 
    :return: 
    """
    all_wineries = Winery.objects.all()
    arguments = {'winery':all_wineries}
    return render(request, "./view_winery.html", arguments)



# class WineList(generics.ListCreateAPIView):
#     """
#     Creates functionality to create and list Wine Model objects bound to the get and post methods
#     """
#
#     queryset = Wine.objects.all()
#     serializer_class = WineSerializer
#
#
#
# class WineDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#
#     """
#     queryset = Wine.objects.all()
#     serializer_class = WineSerializer

# class UserDetail(APIView):
#     """
#
#     """
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'home.html'
#
#     def get(self, request):
#         queryset = User.objects.all()
#         return Response({'users': queryset})
