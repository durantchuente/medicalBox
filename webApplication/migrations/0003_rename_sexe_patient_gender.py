# Generated by Django 5.1.2 on 2024-10-14 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApplication', '0002_alter_patient_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='sexe',
            new_name='gender',
        ),
    ]
