from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('forms.html', forms ,name="forms"),
    path('formulariointer.html', intervencion ,name="intervencion"),
    path('formulariotraslado.html', traslado ,name="traslado")
]