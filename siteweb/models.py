from django.db import models
from django.utils import timezone  # ✅ Ajouté

class Reservation(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    date = models.DateField()
    heure = models.TimeField()
    nombre_de_personnes = models.IntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.date} à {self.heure}"

class Commande(models.Model):
    nom = models.CharField(max_length=100)
    plat = models.CharField(max_length=100)
    quantite = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)  # ✅ Remplacé auto_now_add

    def __str__(self):
        return f"{self.nom} - {self.plat} x {self.quantite}"

class MessageContact(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"Message de {self.prenom} {self.nom}"

