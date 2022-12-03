from django.shortcuts import render
from familiares_app.models import Familiar
def index(request):
    return render(request, "familiares_app/saludar.html")# Create your views here.

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "familiares_app/familiares.html", {"lista_familiares": lista_familiares})