# Generated by Django 4.2.15 on 2024-08-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policyholder', '0018_alter_historicalpolicyholder_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpolicyholder',
            name='employer_tin',
            field=models.CharField(blank=True, db_column='EmployerTIN', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='policyholder',
            name='employer_tin',
            field=models.CharField(blank=True, db_column='EmployerTIN', max_length=128, null=True),
        ),
    ]
