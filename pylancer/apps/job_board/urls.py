from django.conf.urls import patterns, include, url
from views import JobBoard, AddJob

urlpatterns = patterns('',
    url(r'^$', JobBoard.as_view(), name="job_board"),
    url(r'^add_job/$', AddJob.as_view(), name="add_job")
)
