# Generated by Django 4.1.2 on 2022-10-22 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_darbas_pastabos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='darbuotojas',
            name='imone',
        ),
    ]
