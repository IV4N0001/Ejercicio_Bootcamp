# Generated by Django 4.1.2 on 2022-10-13 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managment',
            old_name='descripcion',
            new_name='direccion',
        ),
    ]
