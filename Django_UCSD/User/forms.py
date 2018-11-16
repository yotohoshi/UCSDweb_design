from django import forms
from User.models import User


class userform(forms.Form):
    name = forms.CharField()
    major = forms.CharField()
    minor = forms.CharField()
    Graduation_year = forms.CharField()
    email = forms.EmailField()


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

