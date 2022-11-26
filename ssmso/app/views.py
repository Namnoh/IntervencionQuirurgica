from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'ssmso/login.html')

def index(request):
    return render(request, 'ssmso/index.html')

def forms(request):
    return render(request, 'ssmso/forms.html')

def intervencion(request):
    return render(request, 'ssmso/formulariointer.html')
    
def traslado(request):
    return render(request, 'ssmso/formulariotraslado.html')

