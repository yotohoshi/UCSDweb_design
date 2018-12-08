from django import forms
from django.core.exceptions import ValidationError

from User.models import User, Major, Degree
from overrides import overrides
from django.core import validators


class NewUserForm(forms.Form):
    f_name = forms.CharField(max_length=100, required=True)
    l_name = forms.CharField(max_length=100, required=True)
    yr_graduation = forms.IntegerField(required=True)
    major = forms.CharField(max_length=100, required=True)
    degree = forms.CharField(max_length=100, required=True)
    contact_email = forms.EmailField()

    def create(self, request):
        yr_graduation_val = True
        major_val = True
        degree_val = True
        email_val = True
        # validate info
        f_name = self.cleaned_data['f_name']

        # TODO Check F_Name

        l_name = self.cleaned_data['l_name']

        # TODO Check L_Name

        # Check yr_graduation
        yr_graduation = self.cleaned_data['yr_graduation']
        if yr_graduation<1970 or yr_graduation>2050:
            self.add_error('yr_graduation', 'Year of graduation must be between 1970 and 2050')
            yr_graduation_val = False

        # Check major
        major = self.cleaned_data['major']
        major_obj = Major.objects.get(major=major)
        if major_obj is None:
            self.add_error('major', 'Please choose from valid majors')
            major_val = False

        # Check Degree
        degree = self.cleaned_data['degree']
        degree_obj = Degree.objects.get(degree=degree)
        if degree_obj is None:
            self.add_error('degree', 'Please choose from valid degrees')
            degree_val = False

        # Check email
        contact_email = self.cleaned_data['contact_email']
        try:
            validators.validate_email(contact_email)
            email_val = True

        except ValidationError:
                self.add_error('contact_email', 'Please use a valid contact email')
                email_val = False

        if yr_graduation_val and major_val and degree_val and email_val:
            # if invalid info
            account = request.user
            try:
                usr = User.objects.create(F_Name=f_name,
                                        L_Name=l_name,
                                        yr_graduation=yr_graduation,
                                        major=major_obj,
                                        degree=degree_obj,
                                        contact_email=contact_email,
                                        acc=account)
                if usr is not None:
                    usr.save()
                    return usr
                else:
                    self.add_error(None, 'Oops! something went wrong, please try again!')
                    return None
            except:
                self.add_error('contact_email', 'This email is already in use')
                return None

        else:
            return None


class SearchResultForm(forms.Form):
    name = forms.CharField(max_length='200', required=True)
