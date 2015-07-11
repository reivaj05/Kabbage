from django.conf.urls import patterns, url
from .views import IndexView, SearchFormView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^search/$', SearchFormView.as_view(), name='search'),
)
