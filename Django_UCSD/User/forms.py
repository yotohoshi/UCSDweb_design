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


        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('F_Name', 'L_Name', 'yr_graduation', 'major', 'degree', 'contact_email', "register_email", "password")

        #fields = '__all__'
