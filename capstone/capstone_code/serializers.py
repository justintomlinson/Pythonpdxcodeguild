from django.contrib.auth.models import User, Group
from rest_framework import serializers
from capstone_code.models import Wine, Winery, Cellar



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
        model = Wine
        fields = ('url', 'id', 'wine_name', 'winery_name', 'varietal', 'barcode', 'price', 'quantity')

class WinerySerializer(serializers.HyperlinkedModelSerializer):
    """
    
    """
    class Meta:
        model = Winery
        fields = ('url', 'id', 'winery_name', 'winery_addr', 'winery_phn')




class CellarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cellar
        fields = ('id', 'wine_name', 'winery_name')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, 'user'):
            user = request.user
            user.save()
        cellar = CellarSerializer(wine_name=validated_data['wine_name'],
                         winery_name=validated_data['winery_name'],
                         user=validated_data['user'])
        cellar.save()
        return cellar

