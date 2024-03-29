from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Dans le fichier models.py de votre application parking


class Place(models.Model):
    numero = models.IntegerField(unique=True)
    occupee = models.BooleanField(default=False)
    utilisateur = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.occupee:
            return f"Place {self.numero} - Occupée par {self.utilisateur.username}"
        else:
            return f"Place {self.numero} - Libre"
