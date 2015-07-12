from django.test import TestCase
from common.forms import SearchForm


class TestSearchForm(TestCase):

    def test_form_fields(self):
        form = SearchForm
        form_fields = ['search_criteria', 'query']
        self.assertEqual(
            form.base_fields.keys(),
            form_fields,
            'Expected form fields to be equal to base form fields'
        )

    def test_form_with_valid_data_provided(self):
        form_data = {
            'query': 'test_query',
            'search_criteria': ['T', 'W']
        }
        form = SearchForm(data=form_data)
        self.assertTrue(
            form.is_valid(),
            'Expected form to be valid with correct data provided'
        )

    def test_form_with_invalid_data_provided(self):
        form_data = {
            'query': '',
            'search_criteria': ''
        }
        form = SearchForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            'Expected form to be invalid with incorrect data provided'
        )
