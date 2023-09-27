from django.db import models

# Create your models here.
from django.db import models
from entreprise.models import entreprise  

class JobListing(models.Model):
    entreprise = models.ForeignKey(entreprise, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)
    contract_type = models.CharField(max_length=100, blank=True, null=True)
    experience_required = models.CharField(max_length=100, blank=True, null=True)
    education_required = models.CharField(max_length=100, blank=True, null=True)
    languages_required = models.CharField(max_length=255, blank=True, null=True)
    skills_required = models.TextField(blank=True, null=True)
    job_category = models.CharField(max_length=100, blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_website = models.URLField(max_length=200, blank=True, null=True)
    job_status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('closed', 'Closed'),
            ('pending', 'Pending'),
        ],
        default='active',
    )

    def __str__(self):
        return self.title
