# Generated by Django 4.1.2 on 2022-10-22 13:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_darbas_pastabos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darbas',
            name='pastabos',
            field=tinymce.models.HTMLField(verbose_name='Pastabos'),
        ),
    ]
