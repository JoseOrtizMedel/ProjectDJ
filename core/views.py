from django.shortcuts import render

# Create your views here.

def principal(request):
    return render (request, 'core/PaginaPrincipal.html')

def contacto(request):
    return render(request, 'core/Contacto.html')