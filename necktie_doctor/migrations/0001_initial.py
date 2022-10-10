# Generated by Django 4.0.3 on 2022-10-06 02:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('price', models.PositiveIntegerField()),
                ('about', models.TextField()),
                ('address', models.TextField()),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True, verbose_name='Latitude')),
                ('lng', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True, verbose_name='Longitude')),
                ('public_holiday', models.CharField(choices=[('U', 'Unknown'), ('O', 'Opened'), ('C', 'Closed')], default='U', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('category', models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='necktie_doctor.category')),
                ('district', models.ForeignKey(db_column='district', null=True, on_delete=django.db.models.deletion.SET_NULL, to='necktie_doctor.district')),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='WorkingHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Public Holiday')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('doctor', models.ForeignKey(blank=True, db_column='doctor', on_delete=django.db.models.deletion.CASCADE, related_name='operating_hours', to='necktie_doctor.doctor')),
            ],
            options={
                'db_table': 'working_hour',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, max_length=100)),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='necktie_doctor.doctor')),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='necktie_doctor.doctor')),
            ],
            options={
                'db_table': 'experience',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='necktie_doctor.doctor')),
            ],
            options={
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=100)),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='language', to='necktie_doctor.doctor')),
            ],
            options={
                'db_table': 'language',
            },
        ),
    ]