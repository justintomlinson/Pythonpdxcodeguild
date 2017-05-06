from django.contrib.auth.models import User, Group
from rest_framework import serializers
from capstone_code.models import Wine, Winery, Cellar


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    
    """

    class Meta:
        model = User
        fields =('url', 'id', 'username', 'email', 'wine', 'groups',)



class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'id', 'name')

class WineSerializer(serializers.HyperlinkedModelSerializer):
    """
    
    """
    owner = serializers.ReadOnlyField(source = 'owner.username')
    #Optional highlight setup here
        model = Wine
        fields = ('url', 'id', 'wine_name', 'winery_name', 'varietal', 'price', 'quantity')

class WinerySerializer(serializers.HyperlinkedModelSerializer):
    """
    
    """


    class Meta:
        model = Winery
        fields = ('url', 'winery_name', 'winery_addr', 'winery_phn')

class CellarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cellar
        fields = ('url', 'wine_name', 'winery_name', 'username')
