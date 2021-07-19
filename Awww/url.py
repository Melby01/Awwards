from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^registartion', views.register, name='register'),
    url(r'^',views.index,name='index'),
    url(r'^search$',views.search,name='search'),
    url(r'^profile$',views.new_profile,name='new_profile'),
    url(r'^upload_project',views.upload_project,name='upload_project'),
    url(r'^project$',views.project,name='project')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
