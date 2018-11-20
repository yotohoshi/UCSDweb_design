from django import forms
from User.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('F_Name', 'L_Name', 'yr_graduation', 'major', 'degree', 'contact_email')
