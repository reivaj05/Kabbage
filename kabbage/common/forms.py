from django import forms
from django.utils.translation import ugettext_lazy as _

SEARCH_CHOICES = (
    ('T', 'Twitter'),
    ('W', 'Wikipedia'),
)


class SearchForm(forms.Form):
    search_criteria = forms.MultipleChoiceField(
        label=_('Sites available'),
        choices=SEARCH_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    query = forms.CharField(
        max_length=100,
        label=_('Search'),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.add_placeholder(
            self.fields['query'],
            _('Insert your search here'))

    def add_placeholder(self, field, placeholder):
        field.widget.attrs['placeholder'] = placeholder
