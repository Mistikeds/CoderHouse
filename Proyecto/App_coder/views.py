from django.shortcuts import render, get_object_or_404
from django.views import View
from App_coder.models import Persona
from App_coder.forms import PersonaForm

class ListarPersonas(View):
    template_name= "ejemplo/lista_de_personas.html"

    def get(self, request):
        personas= Persona.objects.all()
        return render(request, self.template_name,{"personas": personas})

class CargarPersonas(View):
    template_name= "ejemplo/agregar_persona.html"
    form_class= PersonaForm
    initial = {'nombre':"", 'apellido':"",'fecha_nacimiento':""}
# get muestra formulario/lista
    def get(self, request):
        form = self.form_class(initial=self.initial) #initial sirve para que inicie vacio
        return render(request, self.template_name,{"form":form})

# post permite guardar los datos ingresados x el usuario

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            #una vez cargado hay que limpiar para que los campos esten vacios (initial)
        return render(request, self.template_name,{"form":form})

class ActualizarPersonas(View):
    template_name= "ejemplo/actualizar_persona.html"
    success_template = "ejemplo/exito.html"
    form_class= PersonaForm
    initial = {'nombre':"", 'apellido':"",'fecha_nacimiento':""}

    def get(self, request, pk): #pk o id
        persona = get_object_or_404(Persona, pk=pk) #filtro x id si no encuentra da return 404
        form = self.form_class(instance=persona) #si existe que se cargue el formulario de la persona
        return render(request, self.template_name,{"form":form, "pk":pk})


    def post(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        form = self.form_class(request.POST, instance=persona) #se pone instance para que guarde.. sino no guarda
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            
        return render(request, self.success_template)
