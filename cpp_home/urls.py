from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('home.views',
    # Examples:
    # url(r'^$', 'cpp_home.views.home', name='home'),
    # url(r'^cpp_home/', include('cpp_home.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'root'),
    url(r'^about$', 'about'),
    url(r'^region/$', 'regions'),
    url(r'^country/$', 'countries'),
    url(r'^country/(?P<country_id>\w+)$', 'country'),

)

urlpatterns += patterns('dsm.views',
    url(r'^dsm/$', 'root'),
    url(r'^dsm/about$', 'about'),
    url(r'^dsm/country/(?P<country_id>\w+)$', 'country'),

)
