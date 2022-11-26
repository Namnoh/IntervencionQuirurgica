from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login.html', login, name="login"),
    path('forms.html', forms ,name="forms"),
    path('formulariointer.html', intervencion ,name="intervencion"),
    path('formulariotraslado.html', traslado ,name="traslado")
]