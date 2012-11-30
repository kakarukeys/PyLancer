from django import forms

from models import Job, FreelancerProfile


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['posted_by']

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = FreelancerProfile
        exclude = ['owner']
