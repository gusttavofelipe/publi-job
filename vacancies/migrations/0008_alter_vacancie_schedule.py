# Generated by Django 4.2 on 2023-04-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_alter_vacancie_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancie',
            name='schedule',
            field=models.TextField(verbose_name='Schedule'),
        ),
    ]
