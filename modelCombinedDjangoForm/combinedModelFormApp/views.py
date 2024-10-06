from django.shortcuts import render, redirect
from .models import Job
from combinedModelFormApp.forms.django_forms import JobForm, ApplicationForm

# Create your views here.
def apply_job(request):
    if request.method == 'POST':
        job_form = JobForm(request.POST)
        application_form = ApplicationForm(request.POST)

        if job_form.is_valid() and application_form.is_valid():
            # Save job instance
            job_instance = job_form.save()

            # Create application instance linked to the job
            application_instance = application_form.save(commit=False)
            application_instance.job = job_instance  # Link to job
            application_instance.save()  # Save application

            return redirect('successPage')  # Redirect after success
    else:
        job_form = JobForm()
        application_form = ApplicationForm()

    return render(request, 'apply_job.html', {'job_form': job_form, 'application_form': application_form})


def successPage(req):
    return render(req, "success.html")


