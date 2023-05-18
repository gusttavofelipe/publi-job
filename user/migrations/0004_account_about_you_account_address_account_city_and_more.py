# Generated by Django 4.2 on 2023-05-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_account_schooling'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='about_you',
            field=models.TextField(default=1, verbose_name='About you'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default=1, max_length=255, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(default=1, max_length=50, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='neighborhood',
            field=models.CharField(default=1, max_length=50, verbose_name='Neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=1, max_length=255, verbose_name='Password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='repeat_password',
            field=models.CharField(default=1, max_length=255, verbose_name='Repeat password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default=1, max_length=2, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('TEC', 'Technology'), ('SRV', 'Service'), ('CMC', 'Communication'), ('ACT', 'Accounting'), ('EDC', 'Education'), ('SEC', 'Security')], default=1, max_length=3, verbose_name='Schooling'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='zip_code',
            field=models.IntegerField(default=1, verbose_name='Zip code'),
            preserve_default=False,
        ),
    ]
