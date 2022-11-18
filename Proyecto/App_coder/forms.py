from django import forms
from App_coder.models import Persona

# sirve para generar los formularios deseados
class PersonaForm(forms.ModelForm):
    fecha_nacimiento= forms.DateField(label="fecha de nacimiento", input_formats=["%d/%m/%Y"],
    # widget agrega un tip al usuario para ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder':'30/12/1995'}))

    class Meta: 
        model = Persona
        fields = ('nombre', 'apellido', 'fecha_nacimiento')

