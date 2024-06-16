from django import forms

#formularios de las distintas clases que imparte el gimnasio
class PrincipianteFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class IntermedioFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    peso = forms.IntegerField()
    
class AvanzadoFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    peso = forms.IntegerField()
    nro_combates = forms.IntegerField()
    

    
class ProfesionalFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    peso = forms.IntegerField()
    nro_combates = forms.IntegerField()
    edad = forms.IntegerField()
    
