# Generated by Django 5.0.4 on 2024-04-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(blank=True, verbose_name='Fecha de devolucion'),
        ),
    ]
