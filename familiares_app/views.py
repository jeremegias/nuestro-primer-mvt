from django.shortcuts import render, get_object_or_404
from familiares_app.models import Familiar, Automovil, Mascota
from familiares_app.forms import Buscar
from familiares_app.forms import Buscar, FamiliarForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView# <----- NUEVO IMPORT


def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "familiares_app/familiares.html", {"lista_familiares": lista_familiares})

def buscar(request):
    lista_de_nombre = ["German", "Daniel", "Romero", "Alvaro"]
    query = request.GET['q']
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = "no hay match"
    return render(request, 'familiares_app/buscar.html', {"resultado": resultado})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'familiares_app/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                         'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

     form_class = FamiliarForm
     template_name = 'familiares_app/alta_familiar.html'
     initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

     def get(self, request):
         form = self.form_class(initial=self.initial)
         return render(request, self.template_name, {'form':form})

     def post(self, request):
         form = self.form_class(request.POST)
         if form.is_valid():
             form.save()
             msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
             form = self.form_class(initial=self.initial)
             return render(request, self.template_name, {'form':form, 
                                                         'msg_exito': msg_exito})

         return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'familiares_app/actualizar_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

   # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(instance=familiar)
        return render(request, self.template_name, {'form':form,'familiar': familiar})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST ,instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'familiar': familiar,
                                                        'msg_exito': msg_exito})

            return render(request, self.template_name, {"form": form})


class BorrarFamiliar(View):
    template_name = 'familiares_app/familiares.html'

    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        familiar.delete()
        familiares = Familiar.objects.all()
        return render(request, self.template_name, {'lista_familiares': familiares})




class FamiliarList(ListView):
    model = Familiar
   
class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]
class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"  
class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarDetalle(DetailView):
  model = Familiar  


class MascotaList(ListView):
    model = Mascota
   
class MascotaCrear(CreateView):
  model = Mascota
  success_url = "/panel-mascota"
  fields = ["especie", "nombre", "edad"]
class MascotaBorrar(DeleteView):
  model = Mascota
  success_url = "/panel-familia"  
class MascotaActualizar(UpdateView):
  model = Mascota
  success_url = "/panel-mascota"
  fields = ["especie", "nombre", "edad"]



class AutomovilList(ListView):
  model = Automovil
   
class AutomovilCrear(CreateView):
  model = Automovil
  success_url = "/panel-automovil"
  fields = ["marca", "modelo", "año"]
class AutomovilBorrar(DeleteView):
  model = Automovil
  success_url = "/panel-automovil"  
class AutomovilActualizar(UpdateView):
  model = Automovil
  success_url = "/panel-automovil"
  fields = ["marca", "modelo", "año"]




