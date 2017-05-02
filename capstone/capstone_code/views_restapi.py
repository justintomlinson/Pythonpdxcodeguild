from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from capstone_code.serializers import UserSerializer, GroupSerializer, WineSerializer, WinerySerializer, CellarSerializer
from capstone_code.models import Wine, Winery, Cellar

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups dto be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class WineViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows wine data to be viewed or edited
    """
    queryset= Wine.objects.all()
    serializer_class = WineSerializer

class WineryViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows winery data to be viewed or edited
    """
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer


class CellarViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows personal cellar data to be viewed or edited
    """
    queryset = Cellar.objects.all()
    serializer_class = CellarSerializer
