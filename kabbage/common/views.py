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
        if 'query' and 'search_criteria' in request.GET:
            form = SearchForm(request.GET)
            query = request.GET.get('query')
            sc = request.GET.getlist('search_criteria')
            self.get_data(query, context, 'T' in sc, 'W' in sc)
        context['form'] = form
        return self.render_to_response(self.get_context_data(**context))

    def get_data(self, query, ctx, search_twitter, search_wikipedia):
        if search_twitter:
            self.get_twitter_data(query, ctx)
        if search_wikipedia:
            self.get_wikipedia_data(query, ctx)

    def get_twitter_data(self, query, ctx):
        twitter_api = twython.Twython(settings.TWITTER_API_KEY, access_token=settings.TWITTER_ACCESS_TOKEN)
        try:
            ctx['twitter_results'] = twitter_api.search(q=query)['statuses']
        except twython.TwythonAuthError:
            ctx['twitter_error'] = 'Twitter API authentification error'
        except twython.TwythonRateLimitError:
            ctx['twitter_error'] = 'Rate limit error: Please wait before searching again'
        except twython.TwythonError:
            ctx['twitter_error'] = 'Connection Error'

    def get_wikipedia_data(self, query, ctx):
        # Search wikipedia
        try:
            ctx['wikipedia_results'] = wikipedia.search(query, results=15)
            print ctx['wikipedia_results']
        except (wikipedia.HTTPTimeoutError, ConnectionError):
            ctx['wikipedia_error'] = "Wikipedia is not responding"
