from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User)
    is_open = models.BooleanField(default=True)
    
class FreelancerProfile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True)
    skype_name = models.CharField(max_length=20, blank=True)
    owner = models.OneToOneField(User)
    is_available = models.BooleanField(default=True)
    
