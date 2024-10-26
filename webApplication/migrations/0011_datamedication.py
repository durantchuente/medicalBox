# Generated by Django 4.2.16 on 2024-10-26 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApplication', '0010_alter_medicalbox_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataMedication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.FloatField(max_length=10)),
                ('tendance', models.CharField(choices=[('H', 'High'), ('L', 'Low')], max_length=1)),
                ('DateTime', models.DateTimeField()),
                ('medical_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_entries', to='webApplication.medicalbox')),
            ],
        ),
    ]
