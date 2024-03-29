# Generated by Django 4.0.3 on 2022-10-10 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('necktie_doctor', '0003_alter_doctor_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.ForeignKey(db_column='gender', null=True, on_delete=django.db.models.deletion.SET_NULL, to='necktie_doctor.gender'),
        ),
    ]
