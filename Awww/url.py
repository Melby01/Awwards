from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^registration', views.register, name='register'),
    url(r'^$',views.index,name='index'),

]