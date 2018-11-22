from django import forms
from .models import WORKAUTHS, JOBTYPES
from User.models import Degree

class SearchingForm(forms.Form):
    keyword = forms.CharField(max_length=500)


class FilterForm(forms.Form):
    start_time = forms.DateInput
    end_time = forms.DateInput
    paid = forms.CheckboxInput
    degree = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=Degree.objects.all())
    work_auth = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=WORKAUTHS)
    job_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=JOBTYPES)
