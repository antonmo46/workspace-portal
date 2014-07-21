from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin # UNCOMMENT THIS LINE

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group



admin.autodiscover() # UNCOMMENT THIS LINE, TOO!

urlpatterns = patterns('',
        url(r'^$', include('qaportal.urls')),
        url(r'^index(\d{1}).html', include('qaportal.urls')),              
        url(r'^rango/', include('rango.urls')),
        url(r'^admin/', include(admin.site.urls)),
        )

if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )