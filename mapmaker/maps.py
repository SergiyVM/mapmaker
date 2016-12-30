from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.maps_list, name='maps_list'),
    url(r'^map/(?P<pk>[0-9]+)/$', views.map_editor, name='map_editor'),
    url(r'^POI/new/$', views.POI_new, name='POI_new'),
    url(r'^POI/(?P<pk>[0-9]+)/edit/$', views.POI_edit, name='POI_edit'),
]