from django.shortcuts import render, redirect
from .models import Reservation, MessageContact, Commande

# === PAGES DU SITE ===
def accueil(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def avis(request):
    return render(request, 'avis.html')

def chefs(request):
    return render(request, 'chefs.html')

def apropos(request):
    return render(request, 'apropos.html')

def contact(request):
    if request.method == "POST":
        prenom = request.POST.get("prenom")
        nom = request.POST.get("nom")
        telephone = request.POST.get("telephone")
        message = request.POST.get("message")

        MessageContact.objects.create(
            prenom=prenom,
            nom=nom,
            telephone=telephone,
            message=message
        )

        return redirect('merci_contact')
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def commande(request):
    if request.method == "POST":
        nom = request.POST.get("Nom")
        email = request.POST.get("Email")
        telephone = request.POST.get("Téléphone")
        plat = request.POST.get("plat_commande")

        Commande.objects.create(
            nom=nom,
            email=email,
            telephone=telephone,
            plat_commande=plat
        )

        return redirect('merci_commande')
    return render(request, 'commande.html')

def reservation(request):
    return render(request, 'reservation.html')

def reserver(request):
    if request.method == "POST":
        nom = request.POST.get("Nom")
        email = request.POST.get("Email")
        telephone = request.POST.get("Téléphone")
        date = request.POST.get("Date")
        heure = request.POST.get("Heure")
        nb_pers = request.POST.get("Nombre_de_personnes")

        Reservation.objects.create(
            nom=nom,
            email=email,
            telephone=telephone,
            date=date,
            heure=heure,
            nombre_de_personnes=nb_pers
        )

        return redirect('merci')
    return redirect('reservation')


# === VUES DE REMERCIEMENT ===
def merci(request):
    return render(request, 'merci.html')

def merci_contact(request):
    return render(request, 'merci_contact.html')

def merci_commande(request):
    return render(request, 'merci_commande.html')

def merci_inscription(request):
    return render(request, 'merci_inscription.html')


def contact(request):
    if request.method == "POST":
        prenom = request.POST.get("prenom")
        nom = request.POST.get("nom")
        telephone = request.POST.get("telephone")
        message = request.POST.get("message")

        # Enregistrement dans la base de données
        MessageContact.objects.create(
            prenom=prenom,
            nom=nom,
            telephone=telephone,
            message=message
        )

        return redirect('merci_contact')  # redirige vers la page de remerciement
    return render(request, 'contact.html')
