# Generated by Django 5.0.2 on 2024-02-29 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("occupation", "0001_initial"),
        ("state", "0004_state_name"),
        ("vacancies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacancy",
            name="occupation_area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="occupation.occupation"
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="state.state"
            ),
        ),
    ]
