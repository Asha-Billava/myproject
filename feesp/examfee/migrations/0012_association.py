# Generated by Django 3.2.4 on 2021-07-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examfee', '0011_auto_20210721_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Association', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Association list',
                'db_table': 'Associations',
            },
        ),
    ]
