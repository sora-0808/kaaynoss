from django import forms
from .models import Reservation, Commande, MessageContact

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class MessageContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = '__all__'
