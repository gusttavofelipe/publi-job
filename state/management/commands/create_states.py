from django.core.management.base import BaseCommand
from state.models import State


class Command(BaseCommand):
    help = "Adds Brazilian states to the database"

    def handle(self, *args, **kwargs):
        brazilian_states = [
            ("Acre"),
            ("Alagoas"),
            ("Amapá"),
            ("Amazonas"),
            ("Bahia"),
            ("Ceará"),
            ("Distrito Federal"),
            ("Espírito Santo"),
            ("Goiás"),
            ("Maranhão"),
            ("Mato Grosso"),
            ("Mato Grosso do Sul"),
            ("Minas Gerais"),
            ("Pará"),
            ("Paraíba"),
            ("Paraná"),
            ("Pernambuco"),
            ("Piauí"),
            ("Rio de Janeiro"),
            ("Rio Grande do Norte"),
            ("Rio Grande do Sul"),
            ("Rondônia"),
            ("Roraima"),
            ("Santa Catarina"),
            ("São Paulo"),
            ("Sergipe"),
            ("Tocantins"),
        ]

        for state_data in brazilian_states:
            if not State.objects.filter(name=state_data).exists():
                state = State.objects.create(name=state_data)
                print(f"State '{state.name}' added successfully.")
            else:
                print(f"State '{state_data[0]}' already exists.")
