from django.shortcuts import render

# Create your views here.
def index(request):
    #print([request])
    return render(request,"aplicacion/index.html")

def saludo(request):
    return render(request,"aplicacion/saludo.html")

def hola(request):
    return render(request,"aplicacion/hola.html")