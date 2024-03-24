from random import randint, choice
from utils import helpers


from django.core.management.base import BaseCommand
from django.db.models import DateTimeField
from django.contrib.auth.models import User

from vacancies.models import Vacancy
from occupation.models import Occupation
from state.models import State
from categories.models import Category


class Command(BaseCommand):
    help = "Add vacancies to the database"

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        states = State.objects.all()
        occupations = Occupation.objects.all()

        for _ in range(10):
            Vacancy.objects.create(
                owner=choice(User.objects.all()),
                name=helpers.random_job(),
                visibility=True,
                category=choice(categories),
                contact_number=helpers.random_phone(),
                contact_whatsapp=helpers.random_phone(),
                contact_email=helpers.random_email(),
                occupation_area=choice(occupations),
                state=choice(states),
                city=helpers.random_city(),
                number=randint(1, 99),
                date_posted=DateTimeField(auto_now=True),
                img=None,
                salary=randint(1000, 10000),
                about_company=helpers.random_text(),
                requirements=helpers.random_text(),
                activities=helpers.random_text(),
                benefits=helpers.random_text(),
                schedule=helpers.random_text(),
            )
