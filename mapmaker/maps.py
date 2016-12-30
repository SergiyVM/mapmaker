from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.maps_list, name='maps_list'),
]