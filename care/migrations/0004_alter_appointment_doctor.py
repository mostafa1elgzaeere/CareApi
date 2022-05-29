# Generated by Django 4.0.2 on 2022-05-20 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0003_alter_appointment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment', to='care.doctor'),
        ),
    ]