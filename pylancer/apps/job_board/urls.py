from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from views import JobBoard, AddJob

urlpatterns = patterns('',
    url(r'^$', JobBoard.as_view(), name="job_board"),
    url(r'^add_job/$', login_required(AddJob.as_view()), name="add_job")
)
