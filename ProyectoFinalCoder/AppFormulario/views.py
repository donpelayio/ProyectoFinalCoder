from django.shortcuts import render
from django.http import HttpResponse
from AppFormulario.models import *
from django.template import loader
from AppFormulario.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


#Clases basadas en vistas

class IntermedioListView(ListView):
    model = Intermedio
    context_object_name = "intermedios"
    template_name = "AppFormulario/intermedio_lista.html"
class IntermedioDetailView(DetailView):
    model = Intermedio
    template_name = "AppFormulario/intermedio_detalle.html"
class IntermedioCreateView(CreateView):
    model = Intermedio
    template_name = "AppFormulario/intermedio_crear.html"
    success_url = reverse_lazy('ListaIntermedio')
    fields = ['nombre','apellido','email','peso']
class IntermedioUpdateView(UpdateView):
    model = Intermedio
    template_name = "AppFormulario/intermedio_editar.html"
    success_url = reverse_lazy('ListaIntermedio')
    fields = ['nombre','apellido','email','peso']
class IntermedioDeleteView(DeleteView):
    model = Intermedio
    template_name = "AppFormulario/intermedio_borrar.html"
    success_url = reverse_lazy('ListaIntermedio')
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario,password=contra)
            
            if user is not None:
                login(request,user)
                
                return render(request, "AppFormulario/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppFormulario/inicio.html", {"mensaje":f"Error, datos incorrectos"})
                
        else:
            return render(request, "AppFormulario/inicio.html", {"mensaje":f"Error, formulario erroneo"})
            
    form = AuthenticationForm()
    
    return render(request,"AppFormulario/login.html", {'form':form})

# views de las templetes de la pagina
def inicio(request):
    
    return render(request,'AppFormulario/inicio.html')

def principiante(request):
    
    return render(request,'AppFormulario/principiante.html')

def intermedio(request):
    
    return render(request,'AppFormulario/intermedio.html')

def avanzado(request):
    
    return render(request,'AppFormulario/avanzado.html')

def profesional(request):
    
    return render(request,'AppFormulario/profesional.html')

#view de los formularios de las distintas clases que se imparten
def principiante(request):
    
    if request.method == 'POST':
        
        miFormulario = PrincipianteFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            principiante = Principiante(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            principiante.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=PrincipianteFormulario()
    return render(request,"AppFormulario/principianteFormulario.html",{"miFormulario":miFormulario})

def intermedio(request):
    
    if request.method == 'POST':
        
        miFormulario = IntermedioFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            intermedio = Intermedio(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],peso=informacion['peso'])
            intermedio.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=IntermedioFormulario()
    return render(request,"AppFormulario/intermedioFormulario.html",{"miFormulario":miFormulario})

def avanzado(request):
    
    if request.method == 'POST':
        
        miFormulario = AvanzadoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            avanzado = Avanzado(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],peso=informacion['peso'],nro_combates=informacion['nro_combates'])
            avanzado.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=AvanzadoFormulario()
    return render(request,"AppFormulario/avanzadoFormulario.html",{"miFormulario":miFormulario})

def profesional(request):
    
    if request.method == 'POST':
    
        miFormulario = ProfesionalFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            profesional = Profesional(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],peso=informacion['peso'],nro_combates=informacion['nro_combates'],edad=informacion['edad'])
            profesional.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=ProfesionalFormulario()
    return render(request,"AppFormulario/profesionalFormulario.html",{"miFormulario":miFormulario})

#busqueda de alumnos principiantes segun su email
def busquedaPrincipiante(request):
    
    return render(request, "busquedaPrincipiante.html",{})

def buscar(request):
    
    if request.GET["email"]:
        
        email = request.GET["email"]
        principiantes = Principiante.objects.get(email=email)
        
        return render(request, "resultadoBusquedaPrincipiante.html",{"principiante":principiantes,"email":email})
    
    else:
        return render(request, 'inicio.html', {"message":"No enviaste el mail correcto"})
    
def leerPrincipiantes (request):
    mis_principiantes = Principiante.objects.all()
    contexto ={"principiantes":mis_principiantes}
    
    return render(request, "AppFormulario/leerPrincipiantes.html",contexto)

def eliminarPrincipiante(request, principiante_nombre):
    
    principiante = Principiante.objects.get(nombre=principiante_nombre)
    principiante.delete()
    
    #vuelvo al menu
    mis_principiantes = Principiante.objects.all()
    contexto = {"principiantes":mis_principiantes}
    return render(request,"AppFormulario/leerPrincipiantes.html",contexto)

def editarPrincipiante(request, principiante_nombre):
    principiante = Principiante.objects.get(nombre=principiante_nombre)
    
    if request.method == 'POST':
        miFormulario = PrincipianteFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            principiante.nombre = informacion['nombre']
            principiante.apellido = informacion['apellido']
            principiante.email = informacion['email']
            
            principiante.save()
            
            return render(request, "AppFormulario/inicio.html")
    else:
        miFormulario = PrincipianteFormulario(initial={'nombre':principiante.nombre, 'apellido':principiante.apellido, 'email':principiante.email})
        
        return render(request, "AppFormulario/editarPrincipiante.html", {"miFormulario":miFormulario, "principiante_nombre":principiante_nombre})
            
