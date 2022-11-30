from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('forms.html', forms ,name="forms"),
    path('formulariointer.html', intervencion ,name="intervencion"),
    path('formulariotraslado.html', traslado ,name="traslado"),
    path('fichaQuirurgica.html', fichaQuirurgica ,name="fichaQuirurgica"),
    path('mostrarTodo.html/', mostrarTodo ,name="mostrarTodo"),
    path('editarReg.html/', editarReg ,name="editarReg"),
    path('verReg.html/<id>/', verReg ,name="verReg"),
    path('delReg/<id>/', delReg, name="delReg"),
    path('paginaMantencion.html', pagMantencion, name="paginaMantencion")
]