# Generated by Django 4.2 on 2023-05-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0013_rename_categorie_vacancy_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('surname', models.CharField(max_length=255, verbose_name='Surname')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('whatsapp', models.IntegerField(verbose_name='WhatsApp')),
                ('phone_number', models.IntegerField(verbose_name='Phone number')),
                ('occupation', models.CharField(max_length=255, verbose_name='Occupation')),
                ('schooling', models.CharField(max_length=255, verbose_name='Schooling')),
            ],
        ),
    ]
