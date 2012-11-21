from django import forms

from models import Job


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['posted_by']
