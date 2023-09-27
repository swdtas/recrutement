from django.db import models

# Create your models here.
class Technologie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='technologie_images/', null=True, blank=True)
    
    def __str__(self):
        return self.nom
