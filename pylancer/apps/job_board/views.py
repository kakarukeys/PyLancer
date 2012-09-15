from django.views.generic.list import ListView
from models import Job

# Create your views here.

class JobList(ListView):
    model = Job
    
