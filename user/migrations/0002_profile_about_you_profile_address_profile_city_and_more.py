# Generated by Django 4.2 on 2023-05-22 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_you',
            field=models.TextField(default=1, verbose_name='About you'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=255, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=1, max_length=255, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.CharField(default=1, max_length=255, verbose_name='Neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default=1, max_length=255, verbose_name='Occupation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default=1, verbose_name='Phone number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='schooling',
            field=models.CharField(choices=[('TEC', 'Technology'), ('SRV', 'Service'), ('CMC', 'Communication'), ('ACT', 'Accounting'), ('EDC', 'Education'), ('SEC', 'Security')], default=1, max_length=3, verbose_name='Schooling'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default=1, max_length=2, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('TEC', 'Technology'), ('SRV', 'Service'), ('CMC', 'Communication'), ('ACT', 'Accounting'), ('EDC', 'Education'), ('SEC', 'Security')], default=1, max_length=3, verbose_name='User type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username_profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='whatsapp',
            field=models.IntegerField(default=1, verbose_name='WhatsApp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='zip_code',
            field=models.IntegerField(default=1, verbose_name='Zip code'),
            preserve_default=False,
        ),
    ]
