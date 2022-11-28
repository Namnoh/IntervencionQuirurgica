from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . import models

class regForm(forms.ModelForm):

    class Meta:
        model = models.Paciente
        fields = '__all__'
        widgets = {
            'paRut': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'paRut'
                }
            ),
            'paNombres': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'paNombres'
                }
            ),
            'paApellidos': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'paApellidos'
                }
            ),
            'paCorreoEmerg': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'paCorreoEmerg'
                }
            ),
            'paCirugia': forms.Select(
                attrs = {
                    'class': 'input',
                    'id' : 'paCirugia'
                }
            ),
            'paAlergias': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'paAlergias',
                    'id' : 'inputJean2',
                }
            ),
            'paCirugiasAnteriores': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'paCirugiasAnteriores',
                    'id' : 'inputJean3'
                }
            ),
        }

class interForm(forms.ModelForm):

    class Meta:
        model = models.InfIntervencion
        fields = ['interNombre','interAnestesia', 'interApoyo', 'interCantApoyo', 'interCantApoyo', 'interObs', 'interInsumos']
        widgets = {
            'interNombre': forms.Select(
                attrs = {
                    'class': 'input',
                    'id' : 'interNombre'
                }
            ),
            'interAnestesia': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'interAnestesia'
                }
            ),
            'interApoyo': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'interApoyo'
                }
            ),
            'interCantApoyo': forms.NumberInput(
                attrs = {
                    'class': 'input',
                    'id' : 'inputJean2',
                    'id' : 'interCantApoyo'
                }
            ),
            'interObs': forms.Textarea(
                attrs = {
                    'class': 'input',
                    'rows': '5',
                    'id' : 'inputJean2',
                    'id' : 'interObs',
                }
            ),
            'interInsumos': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'inputJean2',
                    'id' : 'interInsumos',
                }
            ),
        }

class trasForm(forms.ModelForm):

    class Meta:
        model = models.InfTraslado
        fields = ['trasEquipo','trasSala', 'trasObs']
        widgets = {
            'trasEquipo': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'trasEquipo'
                }
            ),
            'trasSala': forms.TextInput(
                attrs = {
                    'class': 'input',
                    'id' : 'trasSala'
                }
            ),
            'trasObs': forms.Textarea(
                attrs = {
                    'class': 'input',
                    'rows': '5',
                    'id' : 'trasObs',
                }
            ),
        }