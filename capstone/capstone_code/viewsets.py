# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from capstone_code.serializers import UserSerializer, GroupSerializer, WineSerializer, WinerySerializer, \
#                                         CellarSerializer
# from capstone_code.models import Wine, Winery, Cellar
# from rest_framework.response import Response
# from rest_framework import renderers
#
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class WineViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update`, `destroy`, and `highlight` action.
#     """
#     queryset = Wine.objects.all()
#     serializer_class = WineSerializer
#
#
#
#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)
#
#
#
# class WineryViewSet(viewsets.ModelViewSet):
#     """
#      API endpoint that allows winery data to be viewed or edited
#     """
#     queryset = Winery.objects.all()
#     serializer_class = WinerySerializer
#
#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)
#
#
# class CellarViewSet(viewsets.ModelViewSet):
#     """
#      API endpoint that allows personal cellar data to be viewed or edited
#     """
#     queryset = Cellar.objects.all()
#     serializer_class = CellarSerializer
#
#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)
