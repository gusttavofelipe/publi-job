# Generated by Django 4.2 on 2023-04-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancie',
            name='about_company',
            field=models.TextField(default=1, verbose_name='Sobre a empresa'),
            preserve_default=False,
        ),
    ]
