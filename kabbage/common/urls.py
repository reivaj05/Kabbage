from django.conf.urls import patterns, url
from .views import IndexView, SearchView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^search/$', SearchView.as_view(), name='search'),
)
