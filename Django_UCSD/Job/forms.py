from django import forms


class SearchForm(forms.Form):

    keyword = forms.CharField(label='Keyword', max_length=500)
    company_name = forms.CharField(label='Company_name', max_length=200)
    #major = forms.D
    #degree =
    #start_time =
    #end_time =
