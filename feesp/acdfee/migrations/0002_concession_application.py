# Generated by Django 3.2.6 on 2021-09-04 16:18

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acdfee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='concession_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('name', models.CharField(default='xyz', max_length=30)),
                ('roll_no', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('year', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('typeOfconcession', models.CharField(blank=True, max_length=70, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='concreceipts/')),
                ('approve', models.CharField(blank=True, choices=[('A', 'Accept'), ('R', 'Reject')], default=None, max_length=128, null=True)),
                ('date_of_application', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'View Concession application',
                'db_table': 'concession_application',
            },
        ),
    ]