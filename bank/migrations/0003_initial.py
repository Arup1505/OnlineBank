# Generated by Django 4.2.3 on 2023-08-22 11:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0002_delete_transection_delete_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_no', models.CharField(max_length=15)),
                ('tac_no', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('reference', models.CharField(max_length=200)),
                ('tr_id', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('debit', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
            options={
                'db_table': 'Transection',
            },
        ),
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Middle_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('Ph_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=30)),
                ('District', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=30)),
                ('Pin', models.IntegerField()),
                ('Aadhaar', models.IntegerField()),
                ('PAN', models.CharField(max_length=15)),
                ('passport', models.CharField(max_length=20)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=15)),
                ('mpin', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('question', models.CharField(max_length=60)),
                ('answer', models.CharField(max_length=20)),
                ('ac_no', models.CharField(max_length=15)),
                ('balance', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'User_table',
            },
        ),
    ]