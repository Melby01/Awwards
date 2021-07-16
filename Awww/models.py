from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length =60)
    the_image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length =200)
    link = models.URLField()
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
        return projects
            
    def __str__(self):
        return self.description
    
class Profile(models.Model):
    profile_pic= models.ImageField(upload_to='profile/' )
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    more_info = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return self.bio
    
    def save_user(self):
        self.save()
        
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
     
    
