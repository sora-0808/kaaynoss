from django.contrib import admin
from .models import Reservation, Commande, MessageContact

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'date', 'heure', 'nombre_de_personnes', 'date_ajout')
    list_filter = ('date',)
    search_fields = ('nom', 'email', 'telephone')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'plat', 'quantite', 'date')
    list_filter = ('date',)
    search_fields = ('nom', 'plat')

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'telephone', 'message')
    search_fields = ('prenom', 'nom', 'telephone')



