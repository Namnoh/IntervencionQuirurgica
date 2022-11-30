from django.shortcuts import render, redirect
from . import models
from . forms import regForm, interForm, trasForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'ssmso/index.html')

# FORMULARIO REGISTRO DE PACIENTE

def forms(request):
    if request.method == 'POST':
        reg_form = regForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()

            paciente = models.Paciente.objects.get(paRut=request.POST['paRut'])
            reg = models.RegRecepcion(regRecepPac=paciente)
            reg.save()

            messages.success(request, "Registro guardado correctamente")
            return redirect('intervencion')
        else:
            messages.error(request, "Revise sus datos e intentelo nuevamente")
    else:
        reg_form = regForm()
    return render(request, 'ssmso/forms.html', {'reg_form' : reg_form})

# FORMULARIO INTERVENCIÓN

def intervencion(request):
    if request.method == 'POST':
        inter_form = interForm(request.POST)
        if inter_form.is_valid():
            
            cirugia = models.Cirugia.objects.get(cirugiaId=request.POST['interNombre'])

            reg = models.RegRecepcion.objects.last()
            inter = models.InfIntervencion(interNombre=cirugia, interAnestesia=inter_form.cleaned_data['interAnestesia'], interApoyo=inter_form.cleaned_data['interApoyo'], interCantApoyo=inter_form.cleaned_data['interCantApoyo'], interObs=inter_form.cleaned_data['interObs'], interInsumos=inter_form.cleaned_data['interInsumos'], interRecep=reg)
            
            inter.save()
            
            messages.success(request, "Registro guardado correctamente")
            return redirect('traslado')
        else:
            messages.error(request, "Revise sus datos e intentelo nuevamente")
    else:
        inter_form = interForm()
    return render(request, 'ssmso/formulariointer.html', {'inter_form' : inter_form})

# FORMULARIO TRASLADO

def traslado(request):
    if request.method == 'POST':
        tras_form = trasForm(request.POST)
        if tras_form.is_valid():

            reg = models.RegRecepcion.objects.last()

            try:
                inter = models.InfIntervencion.objects.get(interRecep = reg.regRecepId)
            except:
                var_exists = False
            else:
                var_exists = True

            if var_exists == True :
                inter = models.InfIntervencion.objects.get(interRecep = reg.regRecepId)
                tras = models.InfTraslado(trasEquipo=tras_form.cleaned_data['trasEquipo'], trasSala=tras_form.cleaned_data['trasSala'], trasObs=tras_form.cleaned_data['trasObs'], trasRecep=reg, trasInter=inter)
            else :
                tras = models.InfTraslado(trasEquipo=tras_form.cleaned_data['trasEquipo'], trasSala=tras_form.cleaned_data['trasSala'], trasObs=tras_form.cleaned_data['trasObs'], trasRecep=reg)
            
            tras.save()

            tras = models.InfTraslado.objects.last()
            inter = tras.trasInter

            if inter :
                intervencion = True
            else :
                intervencion = False

            if intervencion :
                bitacora = models.RegQuirurgico(regQuiRec=reg, regQuiInter=inter, regQuiTras=tras)
            else :
                bitacora = models.RegQuirurgico(regQuiRec=reg, regQuiTras=tras)
            
            bitacora.save()

            regQui = models.RegQuirurgico.objects.last()

            context = {
                'r' : regQui
            }
            return render(request, 'ssmso/fichaQuirurgica.html', context)
        else:
            messages.error(request, "Revise sus datos e intentelo nuevamente")
    else:
        tras_form = trasForm()
    return render(request, 'ssmso/formulariotraslado.html', {'tras_form' : tras_form})

# MOSTRAR FINAL

def fichaQuirurgica(request):
    return render(request, 'ssmso/fichaQuirurgica.html')

# MOSTRAR TODOS

def mostrarTodo(request):
    reg = models.RegQuirurgico.objects.all()
    context = {
        'reg': reg
    }
    return render(request, 'ssmso/mostrarTodo.html', context)

#  ELIMINAR UN REGISTRO

def delReg(request, id):
    regQ = models.RegQuirurgico.objects.get(regQuiId=id)
    regQ = regQ.regQuiRec.regRecepPac.paRut
    regQ = models.Paciente.objects.get(paRut=regQ)
    regQ.delete()
    messages.success(request, "Ficha Eliminada Correctamente")
    return redirect('mostrarTodo')

# VER REGISTRO QURÚRGICO
def verReg(request, id):
    regQ = models.RegQuirurgico.objects.get(regQuiId=id)
    return render(request, 'ssmso/verReg.html', {'r' : regQ})


def editarReg(request):
    return render(request, 'ssmso/editarReg.html')

def pagMantencion(request):
    return render(request, 'ssmso/paginaMantencion.html')
