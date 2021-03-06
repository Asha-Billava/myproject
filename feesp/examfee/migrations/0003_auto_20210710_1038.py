# Generated by Django 3.2.4 on 2021-07-10 05:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examfee', '0002_alter_sublist_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='examfeepaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('roll_no', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('sem', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)])),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Student who has paid exam fee?',
                'db_table': 'Exampaid',
            },
        ),
        migrations.AlterField(
            model_name='sublist',
            name='fee',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sublist',
            name='sem',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)]),
        ),
    ]
