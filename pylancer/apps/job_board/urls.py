from django.conf.urls import patterns, include, url
from views import JobBoard

urlpatterns = patterns('',
    url(r'^$', JobBoard.as_view()),
    
)
