# Generated by Django 5.1.2 on 2024-10-14 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
    ]
