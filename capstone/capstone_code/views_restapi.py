from capstone_code.serializers import WineSerializer, WinerySerializer, CellarSerializer, UserSerializer
from capstone_code.models import Wine, Winery, Cellar
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import renderers


# Come back to this if handling permissions and Authentication
# class UserList (generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class WineList(generics.ListCreateAPIView):
    """
    Creates functionality to create and list Wine Model objects bound to the get and post methods
    """

    queryset = Wine.objects.all()
    serializer_class = WineSerializer



class WineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    
    """
    queryset = Wine.objects.all()
    serializer_class = WineSerializer




@api_view(['GET'])
def api_root(request, format=None):
     return Response({
         'users': reverse('user-list', request=request, format=format)})
        #recreate for the other models
        #'wines':








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

