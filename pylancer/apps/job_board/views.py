from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson as json
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError

from models import Job, FreelancerProfile
from forms import AddJobForm, AddProfileForm

# Create your views here.

class JobList(generic.list.BaseListView):
    """A list of jobs"""
    model = Job
    
    def render_to_response(self, context):
        return context  #not rendering any template, the context is used in another view.
        
class FreelancerProfileList(generic.list.BaseListView):
    """A list of freelancer profiles"""
    model = FreelancerProfile
    
    def render_to_response(self, context):
        return context
        
class JobBoard(generic.base.TemplateView):
    template_name = "job_board/job_board.html"
    
    def __init__(self, **kwargs):
        super(JobBoard, self).__init__(**kwargs)
        
        #components
        self.job_list_view = JobList.as_view()
        self.freelancer_profile_list_view = FreelancerProfileList.as_view()
        
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        #the contexts for the two lists
        context["job_list"] = self.job_list_view(request, *args, **kwargs)
        context["freelancer_profile_list"] = self.freelancer_profile_list_view(request, *args, **kwargs)
        return self.render_to_response(context)
        
class AddJob(generic.edit.CreateView):
    model = Job
    form_class = AddJobForm
    initial = {"title": "Ninja Programmer"}
    success_url = reverse_lazy("job_board") #after adding, redirect to job board page
    template_name = "job_board/add_job.html"
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        self.object = form.save()
        
        data = {
            "status": "success",
            "location": str(self.success_url),
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
        
    def form_invalid(self, form):
        ctx = RequestContext(self.request, self.get_context_data(form=form))
        data = {
            "status": "failed",
            "html": render_to_string(self.template_name, ctx),
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
        
class AddProfile(generic.edit.CreateView):
    model = FreelancerProfile
    form_class = AddProfileForm
    initial = {}
    success_url = reverse_lazy("job_board") #after adding, redirect to job board page
    template_name = "job_board/add_profile.html"
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        
        try:
            self.object = form.save()
        except IntegrityError:
            data = {
                "status": "failed",
                "html": "Error when creating profile",
            }
        else:
            data = {
                "status": "success",
                "location": str(self.success_url),
            }
        return HttpResponse(json.dumps(data), content_type="application/json")
        
    def form_invalid(self, form):
        ctx = RequestContext(self.request, self.get_context_data(form=form))
        data = {
            "status": "failed",
            "html": render_to_string(self.template_name, ctx),
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
        
