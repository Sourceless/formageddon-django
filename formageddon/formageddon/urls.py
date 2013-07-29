from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contact_sen$', 'contact_senator.views.contact', name='contact_sen'),
    # Examples:
    # url(r'^$', 'formageddon.views.home', name='home'),
    # url(r'^formageddon/', include('formageddon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
