# Generated by Django 4.2 on 2023-04-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0008_vacancie_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancie',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
