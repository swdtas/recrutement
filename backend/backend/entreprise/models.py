from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser, Group
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Adresse e-mail')
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_user_entreprise_set', 
        verbose_name='Groups',
        help_text='Groups for the user'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_entreprise_set',
        verbose_name='Permissions',
        help_text='Permissions for the user'
    )

    def __str__(self):
        return self.username




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

class profilentreprise(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    site_web = models.URLField()
    logo = models.ImageField(
        upload_to='logos/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        help_text='Formats autorisés : JPG, JPEG, PNG. Taille maximale : 1 Mo.'
    )
    secteur_activite = models.CharField(max_length=100, null=True, blank=True)
    date_creation = models.DateField(null=True, blank=True)
    contacts = models.ManyToManyField(Contact, related_name='entreprise', blank=True)
    domaines_d_activite = models.ManyToManyField(DomaineActivite, related_name='entreprise', blank=True)
    services = models.ManyToManyField(Service, related_name='entreprise', blank=True)
    notes = models.TextField(null=True, blank=True) 
    def __str__(self):
        return self.nom
