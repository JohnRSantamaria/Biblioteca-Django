# Generated by Django 5.0.4 on 2024-04-10 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Lector',
                'verbose_name_plural': 'Lectores',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(verbose_name='Fecha de prestamo')),
                ('fecha_devolucion', models.DateField(verbose_name='Fecha de devolucion')),
                ('devuelto', models.BooleanField(default=False)),
                ('lector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lector.lector')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro')),
            ],
        ),
    ]