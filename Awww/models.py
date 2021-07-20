from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.http  import Http404
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField

# Create your models here.

class Projects(models.Model):
    project = models.CharField(max_length =60)
    image = CloudinaryField('image')
    description = models.CharField(max_length =200)
    live_link = models.URLField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def save_projects(self):
        self.save()
    
    def delete_projects(self):
        self.delete()
           
    @classmethod
    def search_by_project_title(cls,search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
     
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def get_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects
    @classmethod
    def get_projects(request, id):
        try:
            project = Projects.objects.get(pk = id)
        except ObjectDoesNotExist:
            raise Http404()
        return  Projects
            
    def __str__(self):
        return self.description
    
class Profile(models.Model):
    profile_pic= CloudinaryField('image' )
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50, blank=False)
    more_info = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return "%s profile" % self.user

    
    def save_profile(self):
        self.save()
        
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
     
    
