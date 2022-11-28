from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . forms import regForm, interForm, trasForm

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

            return redirect('intervencion')
    else:
        reg_form = regForm()
    return render(request, 'ssmso/forms.html', {'reg_form' : reg_form})

# FORMULARIO INTERVENCIÓN

def intervencion(request):
    if request.method == 'POST':
        inter_form = interForm(request.POST)
        if inter_form.is_valid():
            inter_form.save()
            return redirect('traslado')
    else:
        inter_form = interForm()
    return render(request, 'ssmso/formulariointer.html', {'inter_form' : inter_form})

# FORMULARIO TRASLADO

def traslado(request):
    if request.method == 'POST':
        tras_form = trasForm(request.POST)
        if tras_form.is_valid():
            tras_form.save()

            reg = models.RegRecepcion.objects.last()
            inter = models.InfIntervencion.objects.last()
            tras = models.InfTraslado.objects.last()

            if inter.interId == tras.trasId:
                intervencion = True
            
            if intervencion :
                bitacora = models.RegQuirurgico(regQuiRec=reg, regQuiInter=inter, regQuiTras=tras)
            else:
                bitacora = models.RegQuirurgico(regQuiRec=reg, regQuiTras=tras)
            
            bitacora.save()

            return redirect('ssmso/fichaQuirurgica.html')
    else:
        tras_form = trasForm()
    return render(request, 'ssmso/formulariotraslado.html', {'tras_form' : tras_form})

# MOSTRAR FINAL

def fichaQuirurgica(request):
    return render(request, 'ssmso/fichaQuirurgica.html')

# MODIFICAR FORMULARIO RECEPCION

# def modificarFormularioRecepcion(request, id):
#     formularios = get_object_or_404(models, id= id)
#     data = {
        
#         'form': forms(instance = formulario)
#     }
#     if request.method == 'POST':
#         formulario = forms(data = request.POST , instance= formulario, files= request.FiLES) 
#         if formulario.is_valid():
#             formulario.save()
#             data['mensaje'] = "modificado correctamente"
#             return redirect(to="formulariointer.html")
#         data['form'] = formulario
#     return render(request, 'ssmso/forms.html', data)

#MODIFICAR FORMULARIO INTERVENCION

# def modificarFormularioIntervencio(request, id):
#     return render(request, 'ssmso/formulariointer.html')

#MODIFICAR FORMULARIO TRASLADO 

# def modificarFormularioTraslado(request, id):
#     product = Product.objects.get(prodId=id)
#     datos = {
#         'form': prodForm(instance = product),
#         'product': product,
#     }
#     if request.method == 'POST':
#         if request.FILES != None:
#             formulario = prodForm(data=request.POST, instance = product, files = request.FILES)
#         else:
#             formulario = prodForm(data=request.POST, instance = product)

#         if formulario.is_valid():
#             formulario.save()
#             return redirect('showProd')
#     return render(request, 'ssmso/formularioTraslado.html',datos)
    
def editarRecepcion(request):
    context = {
        'reg_form' : regForm(),
        'inter_form' : interForm(),
        'tras_form' : trasForm()
    }
    return render(request, 'ssmso/editarRecepcion.html', context)

