import re
from faker import Faker

fake = Faker()


def random_email() -> str:
    return fake.email()


def random_job() -> str:
    return fake.job()


def random_city():
    return fake.city()


def random_phone():
    return re.sub(r"\D", "", fake.phone_number())


def random_text():
    return fake.text(max_nb_chars=500)
