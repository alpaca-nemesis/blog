#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'crowix.views.index'),
    url(r'^index/', 'crowix.views.index', name='index'),
    url(r'^login/', 'crowix.views.login', name='login'),
    url(r'^logout/', 'crowix.views.logout', name='logout'),
    url(r'^regist/', 'crowix.views.regist', name='regist'),
    url(r'^contact/', 'crowix.views.contact', name='contact'),
    url(r'^message/', 'crowix.views.message', name='message'),
    url(r'^term/', 'crowix.views.term',name='term'),
    url(r'^admin/', include(admin.site.urls)),
)