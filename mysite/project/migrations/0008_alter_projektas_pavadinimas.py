# Generated by Django 4.1.2 on 2022-10-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_alter_darbas_pastabos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projektas',
            name='pavadinimas',
            field=models.CharField(help_text='Projekto pavadinimas', max_length=200, verbose_name='Projekto pavadinimas'),
        ),
    ]