from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('^' + settings.LOGOUT_URL[1:] + '$', logout, {"next_page": "/"}, name="logout"),
    url(r'', include('social_auth.urls')),
    url(r'', include('pylancer.apps.job_board.urls')),
)
