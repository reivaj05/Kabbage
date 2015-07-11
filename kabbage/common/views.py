from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from .forms import SearchForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'common/index.html'


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'common/search.html'
    error_message = 'There was an error in the search'

    def __init__(self, **kwargs):
        pass

    def form_valid(self, form):
        return super(SearchView, self).form_valid(form)

    def get_success_url(self):
        success_url = super(SearchView, self).get_success_url()
        return success_url

    def get(self, request, *args, **kwargs):
        return super(SearchView, self).get(request, *args, **kwargs)
