from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'redigit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /predict/5
    # url(r'^predict/(?P<image>[0-9]+)/$', views.predict, name='predict'),
    url(r'^predict/$', views.predict, name='predict'),
]
