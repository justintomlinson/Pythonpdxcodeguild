"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from capstone_code import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from capstone_code.views import render_winery_form
from capstone_code.views import render_profile
from capstone_code.views import signup
from capstone_code.views import render_wine_form
from capstone_code.views import view_wines
from capstone_code.views import view_winery
#from capstone_code.views import home_page

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'winery', views.WineryViewSet)
router.register(r'wine', views.WineViewSet)
router.register(r'cellar', views.CellarViewSet)


urlpatterns =([
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^silk', include('silk.urls', namespace='silk')),
    url(r'^render_winery_form$', render_winery_form, name='winery_form'),
    url(r'^render_profile$', render_profile, name='home'),
    url(r'^render_wine_form$', render_wine_form, name='add_wine'),
    url(r'^view_wines$', view_wines, name='view_wines'),
    url(r'^view_winery$', view_winery, name='view_winery'),
    #url(r'^home_page$', home_page, name='home_page'),
])