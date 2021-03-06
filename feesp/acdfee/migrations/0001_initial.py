# Generated by Django 3.2.6 on 2021-09-04 15:55

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clgfeepaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('name', models.CharField(default='xyz', max_length=30)),
                ('roll_no', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('year', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt_image', models.FileField(blank=True, null=True, upload_to='cllegeReceipts/')),
                ('date_of_fee', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Students who have paid full clg fee',
                'db_table': 'clgpaid',
            },
        ),
        migrations.CreateModel(
            name='clghalffeepaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('name', models.CharField(default='xyz', max_length=30)),
                ('roll_no', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('year', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt_image', models.FileField(blank=True, null=True, upload_to='cllegeReceipts/')),
                ('date_of_fee', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Students who have paid half clg fee',
                'db_table': 'clghalfpaid',
            },
        ),
        migrations.CreateModel(
            name='crslist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=10)),
                ('year', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('fee', models.IntegerField()),
            ],
            options={
                'verbose_name': 'course list',
                'db_table': 'clgFee',
            },
        ),
        migrations.CreateModel(
            name='eccfee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Libraryfee', models.IntegerField()),
                ('Examfee', models.IntegerField()),
                ('Associationfee', models.IntegerField()),
                ('magzinefee', models.IntegerField()),
                ('annualday', models.IntegerField()),
                ('MUsportsfee', models.IntegerField()),
                ('Admissionfee', models.IntegerField()),
                ('sportfee', models.IntegerField()),
                ('libraryfine', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Set ECC Fee',
                'db_table': 'eccfee',
            },
        ),
        migrations.CreateModel(
            name='set_concession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concession_type', models.CharField(default='xyz', max_length=30)),
                ('percentage_concession', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Set Concession',
                'db_table': 'concession_prcntage',
            },
        ),
    ]
