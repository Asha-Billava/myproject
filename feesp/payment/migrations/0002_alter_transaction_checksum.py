# Generated by Django 3.2.6 on 2021-08-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='checksum',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
