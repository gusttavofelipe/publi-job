# Generated by Django 4.2 on 2023-04-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_vacancie_activities_vacancie_benefits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancie',
            name='salary',
            field=models.CharField(max_length=255, verbose_name='Salary'),
        ),
    ]
