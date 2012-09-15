from django.conf.urls import patterns, include, url
from views import JobList

urlpatterns = patterns('',
    url(r'^$', JobList.as_view()),
    
)
