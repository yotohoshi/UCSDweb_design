from django import forms


class SearchForm(forms.Form):

    keyword = forms.CharField(label='Keyword', max_length=500)
