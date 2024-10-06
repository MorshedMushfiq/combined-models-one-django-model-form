from django import forms
from combinedModelFormApp.models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['applicant_name', 'applicant_email']


class CombinedForm(forms.Form):
    job = JobForm()
    application = ApplicationForm()        