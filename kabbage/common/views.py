from requests import ConnectionError
import twython
import wikipedia
from django.conf import settings
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
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = {}
        if 'query' in request.GET:
            query = request.GET.get('query')
            form = SearchForm(request.GET)
            if 'search_criteria' in request.GET:
                sc = request.GET.getlist('search_criteria')
                self.get_data(query, context, 'T' in sc, 'W' in sc)
        context['form'] = form
        return self.render_to_response(self.get_context_data(**context))

    def get_data(self, query, context, search_twitter, search_wikipedia):
        if search_twitter:
            self.get_twitter_data(query, context)
        if search_wikipedia:
            self.get_wikipedia_data(query, context)

    def get_twitter_data(self, query, context):
        twitter_api = twython.Twython(settings.TWITTER_API_KEY, access_token=settings.TWITTER_ACCESS_TOKEN)
        try:
            context['twitter_results'] = twitter_api.search(q=query)['statuses']
        except twython.TwythonAuthError:
            context['twitter_error'] = 'Twitter API authentification error'
        except twython.TwythonRateLimitError:
            context['twitter_error'] = 'Rate limit error: Please wait before searching again'
        except twython.TwythonError:
            context['twitter_error'] = 'Connection Error'

    def get_wikipedia_data(self, query, context):
        # Search wikipedia
        try:
            context['wikipedia_results'] = wikipedia.search(query, results=15)
        except (wikipedia.HTTPTimeoutError, ConnectionError):
            context['wikipedia_error'] = "Wikipedia is not responding"
