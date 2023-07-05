# Generated by Django 4.2 on 2023-07-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0009_remove_vacancy_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='visibility',
            field=models.BooleanField(default=1, verbose_name='Visible'),
            preserve_default=False,
        ),
    ]
