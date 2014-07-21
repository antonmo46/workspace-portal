from rango import views
from rango.models import Page
from django.conf.urls import patterns, include, url
import tango_with_django_project.settings as SETTINGS

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^code/$', views.code_coverage, name='code_coverage'))