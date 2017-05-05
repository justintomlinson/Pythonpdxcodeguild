from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from capstone_code.serializers import UserSerializer, GroupSerializer, WineSerializer, WinerySerializer, \
                                        CellarSerializer
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

@api_view(['GET', 'POST'])
def wine_list(request):
    """
    List all wines 
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def wine_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        wine = Wine.objects.get(pk=pk)
    except Wine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WineSerializer(wine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WineSerializer(wine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

