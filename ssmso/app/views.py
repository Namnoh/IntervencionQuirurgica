from django.shortcuts import render, redirect
from . import models
from . forms import regForm, interForm, trasForm, userLogin
from django.contrib.auth import authenticate, login

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         user_form = userLogin(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('index')
#     else:
#         user_form = regForm()
#     return render(request, 'registration/login.html', {'user_form' : user_form})

    # if request.method == 'POST':
    #     user_form = userLogin(request.POST)
    #     user_email = request.POST['userRut']
    #     user_pass = request.POST['userPassword']

    #     # user = authenticate(username=user_email, password=user_pass)
    #     user = models.Usuario.objects.filter(userEmail__icontains=user_email)
    #     user = models.Usuario.objects.filter(userPassword__icontains=user_pass)

    #     if user is not None:
    #         # login(request, user)
    #         email = user.userEmail
    #         return render(request, "ssmso/index.html", {'email' : email})
    #     else:
    #         user_form = userLogin()
    #         context = {
    #             "err" : "NO HAY USUARIO",
    #             'user_form' : user_form
    #         }
    #         return render(request, 'registration/login.html', {'context' : context})
    # else:
    #     user_form = userLogin()
    #     context = {
    #         "err" : "NO TIENE POST",
    #         'user_form' : user_form
    #     }
    # return render(request, 'registration/login.html', {'context' : context})

def index(request):
    return render(request, 'ssmso/index.html')

def forms(request):
    if request.method == 'POST':
        reg_form = regForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('intervencion')
    else:
        reg_form = regForm()
    return render(request, 'ssmso/forms.html', {'reg_form' : reg_form})

def intervencion(request):
    if request.method == 'POST':
        inter_form = interForm(request.POST)
        if inter_form.is_valid():
            inter_form.save()
            return redirect('traslado')
    else:
        inter_form = interForm()
    return render(request, 'ssmso/formulariointer.html', {'inter_form' : inter_form})
    
def traslado(request):
    if request.method == 'POST':
        tras_form = trasForm(request.POST)
        if tras_form.is_valid():
            tras_form.save()
            return redirect('traslado')
    else:
        tras_form = trasForm()
    return render(request, 'ssmso/formulariotraslado.html', {'tras_form' : tras_form})