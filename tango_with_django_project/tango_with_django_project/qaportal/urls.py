from qaportal import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index1.html', views.load_view, name='index1'),
    url(r'^index2.html', views.index2, name='index2'),
    url(r'^index3.html', views.index3, name='index3'),
    url(r'^index4.html', views.index4, name='index4'),
    url(r'^$', views.load_view, name='load'))