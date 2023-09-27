from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Adresse e-mail')
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_user_chercheur_set',
        verbose_name='Groups',
        help_text='Groups for the user'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_chercheur_set',
        verbose_name='Permissions',
        help_text='Permissions for the user'
    )

    def __str__(self):
        return self.username


# Modèle de compétence
class Competence(models.Model):
    nom_competence = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom_competence

# Modèle de profil pour les chercheurs d'emploi
class Profilchercheur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        help_text='Formats autorisés : JPG, JPEG, PNG. Taille maximale : 5 Mo.'
    )
    date_naissance = models.DateField(null=True, blank=True)
    ville = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    cv = models.FileField(
        upload_to='cv/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'doc', 'docx'],
            message='Les fichiers autorisés sont au format PDF, DOC ou DOCX.'
        )]
    )
    description = models.TextField(null=True)
    portfolio = models.URLField(max_length=200, null=True, blank=True)
    competence= models.ForeignKey(Competence, on_delete=models.CASCADE)
    experience = models.TextField(null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
