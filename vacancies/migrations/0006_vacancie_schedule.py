# Generated by Django 4.2 on 2023-04-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_alter_vacancie_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancie',
            name='schedule',
            field=models.TextField(default=1, verbose_name='Schedule'),
            preserve_default=False,
        ),
    ]
