# Generated by Django 4.2.16 on 2024-10-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApplication', '0004_medicalbox_notes_alter_medicalbox_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phoneNumber',
            field=models.IntegerField(max_length=255),
        ),
    ]
