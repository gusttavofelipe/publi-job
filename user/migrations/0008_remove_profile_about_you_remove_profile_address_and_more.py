# Generated by Django 4.2 on 2023-05-19 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_account_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about_you',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='repeat_password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='schooling',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='zip_code',
        ),
    ]
