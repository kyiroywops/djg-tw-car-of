from django import forms
from .models import Auto, Ventas, Compradores, Vendedores, Detalles

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
    
    class Meta1:
        model = Ventas
        fields = '__all__'

    class Meta2:
        model = Compradores
        fields = '__all__'
    
    class Meta3:
        model = Vendedores
        fields = '__all__'

    class Meta4:
        model = Detalles
        fields = '__all__'

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'