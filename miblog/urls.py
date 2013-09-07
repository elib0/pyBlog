from django.conf.urls import patterns, include, url
from posts import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miblog.views.home', name='home'),
    # url(r'^miblog/', include('miblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Mapeo de urls
    url(r'^$', views.index, name="home"),
    # url(r'^post/(\d+)/$', views.ajax_single_post, name="single_post"),
    url(r'^post/(\d+)/$', views.single_post, name="single_post"),
    url(r'^comment/(\d+)/$', views.ajax_form_comment_post, name="comment_post"),
    # url(r'^user/new/$', views.user_register, name="register_user"),
)
