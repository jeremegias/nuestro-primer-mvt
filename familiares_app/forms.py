from django import forms
from familiares_app.models import Familiar, Automovil, Mascota

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={"placeholder": "busque algo..."}))

class FamiliarForm(forms.ModelForm):
   class Meta:
     model = Familiar
     fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['especie', 'nombre', 'edad']

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'año']




    

