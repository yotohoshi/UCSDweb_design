from django import forms
from User.models import User, Major, Degree
from overrides import overrides
from django.core import validators


class NewUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['F_Name', 'L_Name', 'yr_graduation', 'major', 'degree', 'contact_email']


class SearchResultForm(forms.Form):

    name = forms.CharField(max_length='200', required=True)
