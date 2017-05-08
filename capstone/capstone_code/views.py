from django.shortcuts import render, redirect
from rest_framework import viewsets
from capstone_code.models import Wine, Winery, Cellar
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from capstone_code.forms import SignUpForm
from capstone_code.serializers import WineSerializer, WinerySerializer, CellarSerializer, UserSerializer, \
                                        GroupSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
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

    render_classes = [TemplateHTMLRenderer]
    template_name = 'view_wines.html'
    serializer_class = WineSerializer
    queryset = Wine.objects.all()

    def get(self, request):
        queryset = Wine.objects.all()
        return Response({'wines':queryset})




    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)



class WineryViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows winery data to be viewed or edited
    """

    render_classes = [TemplateHTMLRenderer]
    template_name = 'view_winery.html'
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer

    def get(self, queryset, request):
        return Response({'winery': queryset})

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


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

# def home_page (request, username):
#
#     user = User.objects.get(username=username)
#     template = get_template('home.html')
#     variables = Context({'username':username})
#     output = template.render(variable)
#     return render(output)

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

class UserDetail(APIView):
    """
    
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})
