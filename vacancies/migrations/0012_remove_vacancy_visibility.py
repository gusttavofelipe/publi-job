# Generated by Django 4.2 on 2023-07-07 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0011_alter_vacancy_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='visibility',
        ),
    ]