from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('chefs/', views.chefs, name='chefs'),
    path('avis/', views.avis, name='avis'),
    path('contact/', views.contact, name='contact'),
    path('apropos/', views.apropos, name='apropos'),
    path('login/', views.login_view, name='login'),
    path('commande/', views.commande, name='commande'),
    path('reservation/', views.reservation, name='reservation'),
     path('reserver/', views.reserver, name='reserver'),
    path('merci/', views.merci, name='merci'),
    path('merci-inscription/', views.merci_inscription, name='merci_inscription'),
    path('merci-contact/', views.merci_contact, name='merci_contact'),
        path('contact/', views.contact, name='contact'),
    path('merci-contact/', views.merci_contact, name='merci_contact'),  
        path('login/', views.login_view, name='login'),
    path('merci-inscription/', views.merci_inscription, name='merci_inscription'), 


     path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('chefs/', views.chefs, name='chefs'),
    path('avis/', views.avis, name='avis'),
    path('contact/', views.contact, name='contact'),
    path('apropos/', views.apropos, name='apropos'),
    path('login/', views.login_view, name='login'),
    path('commande/', views.commande, name='commande'),
    path('reservation/', views.reservation, name='reservation'),
    path('reserver/', views.reserver, name='reserver'),

    # vues de remerciement
    path('merci/', views.merci, name='merci'),
    path('merci-contact/', views.merci_contact, name='merci_contact'),
    path('merci-commande/', views.merci_commande, name='merci_commande'),

    
]



