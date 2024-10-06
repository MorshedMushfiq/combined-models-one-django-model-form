from django.urls import path
from combinedModelFormApp.views import apply_job, successPage

urlpatterns = [
    path('apply/', apply_job, name='job_apply'),
    path('success/', successPage, name='successPage'),
]







