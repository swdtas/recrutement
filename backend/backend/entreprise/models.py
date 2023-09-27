from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.nom

class DomaineActivite(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class entreprise(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    site_web = models.URLField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    secteur_activite = models.CharField(max_length=100, null=True, blank=True)
    date_creation = models.DateField(null=True, blank=True)
    contacts = models.ManyToManyField(Contact, related_name='entreprise', blank=True)
    domaines_d_activite = models.ManyToManyField(DomaineActivite, related_name='entreprise', blank=True)
    services = models.ManyToManyField(Service, related_name='entreprise', blank=True)
    notes = models.TextField(null=True, blank=True) 
    def __str__(self):
        return self.nom
