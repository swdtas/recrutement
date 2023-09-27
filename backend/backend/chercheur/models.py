from django.db import models
# Create your models here.
from django.contrib.auth.models import User
# Modèle de base de données pour les informations complémentaires de l'utilisateur
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    ville = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    description = models.TextField(null=True)
    portfolio = models.URLField(max_length=200, null=True, blank=True)
    competence = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class SocialNetwork(models.Model):
    nom = models.CharField(max_length=50)
    icone = models.ImageField(upload_to='social_icons/')

    def __str__(self):
        return self.nom

class SocialProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reseau = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)
    lien_profil = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.user.username} sur {self.reseau.nom}"
