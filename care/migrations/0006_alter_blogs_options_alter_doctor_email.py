# Generated by Django 4.0.4 on 2022-05-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0005_blogs_doctor_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]