from django import forms
from .models import Equipment, Client, Rental


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'