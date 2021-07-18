from os import name
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^', views.register, name='register'),
    url(r'^login', views.login_request, name='login'),
    url(r'^index$',views.index,name='index'),
    url(r'^search$',views.search,name='search'),
    url(r'^profile$',views.new_profile,name='new_profile')
]