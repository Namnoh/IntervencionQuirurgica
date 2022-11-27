# Generated by Django 4.0.4 on 2022-11-26 21:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infintervencion',
            name='interFecha',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha Intervención'),
        ),
        migrations.AlterField(
            model_name='infintervencion',
            name='interHora',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Hora Intervención'),
        ),
        migrations.AlterField(
            model_name='infintervencion',
            name='interNombre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.cirugia'),
        ),
        migrations.AlterField(
            model_name='inftraslado',
            name='trasFecha',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha Traslado'),
        ),
        migrations.AlterField(
            model_name='inftraslado',
            name='trasHora',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Hora Traslado'),
        ),
        migrations.AlterField(
            model_name='regquirurgico',
            name='regQuiFecha',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha Registro de Quirúrgico'),
        ),
        migrations.AlterField(
            model_name='regquirurgico',
            name='regQuiHora',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Hora Registro de Quirúrgico'),
        ),
        migrations.AlterField(
            model_name='regrecepcion',
            name='regRecepFecha',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha Registro de Recepción'),
        ),
        migrations.AlterField(
            model_name='regrecepcion',
            name='regRecepHora',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Hora Registro de Recepción'),
        ),
    ]