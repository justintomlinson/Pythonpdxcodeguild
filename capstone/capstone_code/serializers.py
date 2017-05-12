from django.contrib.auth.models import User, Group
from rest_framework import serializers
import capstone_code.models as Models
from rest_framework.fields import CurrentUserDefault



class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    
    """

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email')



class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'id', 'name')


class WineSerializer(serializers.HyperlinkedModelSerializer):
    """
        
    """
    class Meta:
        model = Models.Wine
        fields = ('url', 'id', 'wine_name', 'winery_name', 'varietal', 'barcode', 'price', 'quantity')

class WinerySerializer(serializers.HyperlinkedModelSerializer):
    """
    
    """
    class Meta:
        model = Models.Winery
        fields = ('url', 'id', 'winery_name', 'winery_addr', 'winery_phn')




class CellarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Models.Cellar
        fields = ('id', 'wine_name', 'winery_name', 'username')


class CellarUserProfilePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Cellar
        fields = ('id','username', 'wine_name', 'winery_name')

    def create(self, validated_data):
        current_user = self.context['request'].username
        my_wine_name = validated_data["Wine"].wine_name
        wine_local = Models.Wine.objects.get(wine_name = my_wine_name)
        my_winery_name = validated_data["Winery"].winery_name
        winery_local = Models.Wine.objects.get(winery_name = my_winery_name)
        my_cellar_profile = Models.Cellar(
            username = current_user,
            wine_name = self.validated_data["wine_name"],
            winery_name = self.validated_data["winery_name"]
        )
        my_cellar_profile.save()
        return my_cellar_profile

    def update(self):
        my_cellar_profile = Models.User.objects.get(username=CurrentUserDefault())
        my_cellar_profile.wine_name = self.validated_data['wine_name']
        my_cellar_profile.wunery_name = self.validated_data['winery_name']
        my_celar_profile.save()