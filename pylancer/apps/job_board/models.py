from django.db import models
from django.contrib.auth.models import User

CONTRACT_TYPE_CHOICES = (
    ("FT", "fulltime"),
    ("PT", "part-time"), 
    ("FL", "freelance"),
)

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    contract_type = models.CharField(max_length=2, choices=CONTRACT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User)
    employer = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)
    location = models.CharField(max_length=40)
    
    def contract_type_as_html(self):
        """ Use in CSS class """
        if self.contract_type == "FT":
            return "full"
        if self.contract_type == "PT":
            return "part"
        if self.contract_type == "FL":
            return "free"
        return ""

class FreelancerProfile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True)
    skype_name = models.CharField(max_length=20, blank=True)
    owner = models.OneToOneField(User)
    is_available = models.BooleanField(default=True)
    
