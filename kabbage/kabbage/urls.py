from django.conf.urls import patterns, include, url, static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('common.urls', namespace='common')),
)


if settings.DEBUG:
    urlpatterns += static.static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
