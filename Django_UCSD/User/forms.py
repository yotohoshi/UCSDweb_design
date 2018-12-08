from django import forms
from User.models import User, Major, Degree
from overrides import overrides
from django.core import validators


class NewUserForm(forms.Form):
    class Meta:
        model = User
        F_Name = forms.CharField(max_length=100, required=True)
        L_Name = forms.CharField(max_length=100, required=True)
        yr_graduation = forms.IntegerField(required=True)
        major = forms.CharField(max_length=100, required=True)
        degree = forms.CharField(max_length=100, required=True)
        contact_email = forms.EmailField()
        # fields = ['F_Name', 'L_Name', 'yr_graduation', 'major', 'degree', 'contact_email']

    def save(self):
        if self.is_valid():
            usr = User.objects.create(F_Name=self.cleaned_data['F_Name'],
                                      L_Name=self.cleaned_data['L_Name'],
                                      yr_graduation=self.cleaned_data['yr_graduation'],
                                      major=Major.objects.get(major=self.cleaned_data['major']),
                                      degree=Degree.objects.get(degree=self.cleaned_data['degree']),
                                      contact_email=self.cleaned_data['contact_email'])
            usr.save()
            return usr
        else:
            return None


class SearchResultForm(forms.Form):
    name = forms.CharField(max_length='200', required=True)
