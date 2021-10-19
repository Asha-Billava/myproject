# Generated by Django 3.2.4 on 2021-08-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examfee', '0012_association'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examfeepaid',
            name='form_image',
            field=models.FileField(blank=True, null=True, upload_to='examForms/'),
        ),
        migrations.AlterField(
            model_name='examfeepaid',
            name='receipt_image',
            field=models.FileField(blank=True, null=True, upload_to='examReceipts/'),
        ),
    ]