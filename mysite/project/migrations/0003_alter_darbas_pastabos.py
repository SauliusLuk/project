# Generated by Django 4.1.2 on 2022-10-22 10:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_darbas_pavadinimas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darbas',
            name='pastabos',
            field=tinymce.models.HTMLField(blank=True, max_length=2000, verbose_name='Pastabos'),
        ),
    ]
