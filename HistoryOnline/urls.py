from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('HistoryOnline.home.views',
    # Examples:
    # url(r'^$', 'HistoryOnline.views.home', name='home'),
    # url(r'^HistoryOnline/', include('HistoryOnline.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home_screen'),
    )

urlpatterns += patterns('HistoryOnline.mainMap.views',
	url(r'^map/$', 'mapIntro'),
    url(r'^map/(?P<title>\w+)/(?P<fil>\w+)/$', 'mainMap'),
	)

urlpatterns += patterns('HistoryOnline.webdev.views',
    url(r'create_web/$', 'devlist'),
	url(r'^create_web/(?P<title>\w+)/$', 'webdev'),
    url(r'^submit/$', 'submitted'),
	)

urlpatterns += patterns('HistoryOnline.closeup.views',
    url(r'^node/(?P<title>\w+)/(?P<topic>\w+)/$','closeup'),
    )

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )