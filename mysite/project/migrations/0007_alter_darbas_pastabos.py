# Generated by Django 4.1.2 on 2022-10-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_darbas_atsakingas_darbuotojas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darbas',
            name='pastabos',
            field=models.TextField(verbose_name='Pastabos'),
        ),
    ]
