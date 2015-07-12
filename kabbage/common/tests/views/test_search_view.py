from django.test import TestCase
from django.core.urlresolvers import reverse
from common.forms import SearchForm
from common.views import SearchFormView


class TestSearchFormView(TestCase):

    def setUp(self):
        self.search_url = reverse('common:search')

    def test_form_view_class(self):
        form = SearchForm
        view = SearchFormView
        self.assertEqual(
            form,
            view.form_class,
            'Expected form view to be equal to SearchForm class'
        )

    def test_template_used(self):
        response = self.client.get(self.search_url)
        self.assertTemplateUsed(
            response=response,
            template_name='common/search.html'
        )

    def test_view_with_no_query(self):
        response = self.client.get(self.search_url)
        self.assertNotIn(
            'twitter_results',
            response.context,
            'Twitter results not expected to be in context'
        )
        self.assertNotIn(
            'wikipedia_results',
            response.context,
            'Wikipedia results not expected to be in context'
        )

    def test_view_with_twitter_query(self):
        response = self.client.get(
            self.search_url,
            {"query": "Twitter test", "search_criteria": "T"}
        )
        self.assertIn(
            'twitter_results',
            response.context,
            'Twitter results expected to be in context'
        )
        self.assertTrue(
            response.context['twitter_results'],
            'Twitter results not expected to be empty'
        )

    def test_view_with_wikipedia_query(self):
        response = self.client.get(
            self.search_url,
            {"query": "Wikipedia test", "search_criteria": "W"}
        )
        self.assertIn(
            'wikipedia_results',
            response.context,
            'Wikipedia results expected to be in context'
        )
        self.assertTrue(
            response.context['wikipedia_results'],
            'Wikipedia results not expected to be empty'
        )
