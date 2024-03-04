from django.core.management.base import BaseCommand
from occupation.models import Occupation


class Command(BaseCommand):
    help = "Adds Vacancy occupations to the database"

    def handle(self, *args, **kwargs):
        occupation_list = [
            "Technology",
            "Service",
            "Communication",
            "Accounting",
            "Education",
            "Security",
        ]

        for name in occupation_list:
            if not Occupation.objects.filter(name=name).exists():
                occupation = Occupation.objects.create(name=name)
                occupation.save()
                print(f"Occupation '{name}' added successfully.")
            else:
                print(f"Occupation '{name}' already exists.")
