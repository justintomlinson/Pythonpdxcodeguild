from django.contrib.auth.models import User, Group
from rest_framework import serializers
from capstone_code.models import Wine, Winery, Cellar


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields =('url', 'username', 'email', 'groups',)



class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

class WineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Wine
        fields = ('url', 'wine_name', 'winery_name', 'varietal', 'price', 'quantity')

class WinerySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Winery
        fields = ('url', 'winery_name', 'winery_addr', 'winery_phn')

class CellarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cellar
        fields = ('url', 'wine_name', 'winery_name', 'username')
