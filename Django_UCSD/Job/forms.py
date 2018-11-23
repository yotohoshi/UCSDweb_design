from django import forms


AUTH = ['U.S Citizen','Permanent Resident','F-1','H1-B','OPT','CPT','Otherwise Authorized to Work',]
JOBTYPE = ['intern', 'Full Time', 'Part Time', 'Free Lance']
DEGS = ['BS', 'BA', 'MS', 'MA', 'PHD', 'MBA', 'NO LIMITED']


class SearchingForm(forms.Form):
    keyword = forms.CharField(max_length=500)


class FilterForm(forms.Form):
    start_time = forms.CharField(max_length=100, required=False)
    end_time = forms.CharField(max_length=100, required=False)
    paid = forms.BooleanField(required=False)
    degree = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=DEGS, required=False)
    work_auth = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=AUTH, required=False)
    job_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=JOBTYPE, required=False)
