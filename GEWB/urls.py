from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GEWB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('GEWB_app.views',
	url(r'^$', "master", name="home"),
	url(r'^signup$', "signup", name="signup"),
	url(r'^signin$', "signin", name="signin"),
	url(r'^signout$', "signout", name="signout"),
	url(r'^dashboard$', "dashboard", name="dashboard"),
)

urlpatterns += patterns('GEWB_app.api',
    url(r'^emergency/(?P<em_type>\w+)/add/$', "add_emergency", name="emergency_add"),
)
