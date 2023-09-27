from django.db import models
from django.contrib.auth.models import User
from job_listings.models import JobListing
# Create your models here.
APPLICATION_STATUS_CHOICES = (
    ('en_attente', 'En attente'),
    ('acceptée', 'Acceptée'),
    ('refusée', 'Refusée')),
class Candidacture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_listing= models.ForeignKey(JobListing, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    cv = models.FileField(upload_to='cv/')
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES)
    def __str__(self):
        return f'Candidature de {self.user.username} pour {self.job_listing.title}'
