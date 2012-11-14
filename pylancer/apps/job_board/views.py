from django.views.generic.list import BaseListView
from django.views.generic.base import TemplateView

from models import Job, FreelancerProfile

# Create your views here.

class JobList(BaseListView):
    """A list of jobs"""
    model = Job
    
    def render_to_response(self, context):
        return context  #not rendering any template, the context is used in another view.
        
class FreelancerProfileList(BaseListView):
    """A list of freelancer profiles"""
    model = FreelancerProfile
    
    def render_to_response(self, context):
        return context
        
class JobBoard(TemplateView):
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
        
