from os import name
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^', views.register, name='register'),
    url(r'^index$',views.index,name='index'),
    url(r'^serach$',views.search,name='serach')

]