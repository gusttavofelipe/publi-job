from django.core.management.base import BaseCommand
from categories.models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories_list = [
            "All",
            "Trainee",
            "Home Office",
        ]

        for name in categories_list:
            if not Category.objects.filter(name=name).exists():
                category = Category.objects.create(name=name)
                category.save()
                print(f"Category '{name}' added successfully.")
            else:
                print(f"Category '{name}' already exists.")
