from requests import ConnectionError
import twython
import wikipedia
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import FormView, TemplateView
from .forms import SearchForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'common/index.html'


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'common/search.html'
    error_message = 'There was an error in the search'

    def get(self, request, *args, **kwargs):
        self.context = {}
        self.page_twitter = request.GET.get('page_twitter')
        self.page_wikipedia = request.GET.get('page_wikipedia')
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if 'query' in request.GET:
            query = request.GET.get('query')
            form = SearchForm(request.GET)
            self.context['query'] = query
            if 'search_criteria' in request.GET:
                sc = request.GET.getlist('search_criteria')
                self.get_data(query, 'T' in sc, 'W' in sc)
        self.context['form'] = form
        return self.render_to_response(self.get_context_data(**self.context))

    def get_page(self, page, objects):
        paginator = Paginator(objects, 10)
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            objects = paginator.page(paginator.num_pages)
        return objects

    def get_data(self, query, search_twitter, search_wikipedia):
        if search_twitter:
            self.get_twitter_data(query)
        if search_wikipedia:
            self.get_wikipedia_data(query)

    def get_twitter_data(self, query):
        self.context['sct'] = True
        self.context['page_twitter'] = self.page_twitter
        twitter_api = twython.Twython(
            settings.TWITTER_API_KEY,
            access_token=settings.TWITTER_ACCESS_TOKEN
        )
        try:
            self.context['twitter_results'] = twitter_api.search(
                q=query, count=100)['statuses']
            self.context['twitter_results'] = self.get_page(
                self.page_twitter, self.context['twitter_results']
            )
        except twython.TwythonAuthError:
            self.context['twitter_error'] = 'Twitter API authentication error'
        except twython.TwythonRateLimitError:
            self.context['twitter_error'] = 'Rate limit error: Please wait before searching again'
        except twython.TwythonError:
            self.context['twitter_error'] = 'Connection Error'

    def get_wikipedia_data(self, query):
        self.context['scw'] = True
        self.context['page_wikipedia'] = self.page_wikipedia
        try:
            self.context['wikipedia_results'] = wikipedia.search(query, results=100)
            self.context['wikipedia_results'] = self.get_page(
                self.page_wikipedia, self.context['wikipedia_results'])
        except (wikipedia.HTTPTimeoutError, ConnectionError):
            self.context['wikipedia_error'] = "Wikipedia is not responding"
