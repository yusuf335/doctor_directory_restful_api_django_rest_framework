# Generated by Django 4.0.3 on 2022-10-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necktie_doctor', '0002_remove_education_doctor_doctor_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='education',
            field=models.TextField(),
        ),
    ]
