# Generated by Django 4.2 on 2023-06-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_alter_vacancy_occupation_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='occupation_area',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Service', 'Service'), ('Communication', 'Communication'), ('Accounting', 'Accounting'), ('Education', 'Education'), ('Security', 'Security')], max_length=13, verbose_name='Occupation area'),
        ),
    ]
