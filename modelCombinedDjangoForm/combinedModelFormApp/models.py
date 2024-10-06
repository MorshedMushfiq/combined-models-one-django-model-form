from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()

    def __str__(self):
        return f"{self.applicant_name} applied for {self.job.title}"

