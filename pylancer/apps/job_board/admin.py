from django.contrib import admin
from .models import Job, FreelancerProfile

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'created_at', 'posted_by', 'is_open']

class FreelancerProfileAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'is_available']

admin.site.register(Job, JobAdmin)
admin.site.register(FreelancerProfile, FreelancerProfileAdmin)
