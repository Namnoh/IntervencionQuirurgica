# Generated by Django 4.0.4 on 2022-11-29 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inftraslado',
            name='trasInter',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.infintervencion'),
        ),
        migrations.AlterField(
            model_name='regquirurgico',
            name='regQuiInter',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.infintervencion'),
        ),
    ]
