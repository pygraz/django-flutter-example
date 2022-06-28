import random
from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import GenderChoices, Person
from personbook.settings import DEMO_PASSWORD

MALE_FIRST_NAMES = [
    "Michael",
    "Christoper",
    "Matthew",
    "Joshua",
    "Jacob",
    "Nicholas",
    "Andrew",
    "Daniel",
    "Tyler",
    "Joseph",
]
FEMALE_FIRST_NAMES = [
    "Jessica",
    "Ashley",
    "Emily",
    "Sarah",
    "Samantha",
    "Amanda",
    "Brittany",
    "Elizabeth",
    "Taylor",
    "Megan",
]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]


class Command(BaseCommand):
    help = "Make database with demo data"

    def handle(self, *args, **options):
        self._create_demo_admin_if_not_exists()
        self._create_demo_persons()
        self.stdout.write(self.style.SUCCESS("Successfully added demo data"))

    def _create_demo_admin_if_not_exists(self, username: str = "admin"):
        with transaction.atomic():
            result = User.objects.select_for_update().filter(username=username).first()
            if result is None:
                self.stdout.write(f"Adding demo admin {username!r}")
                User.objects.create_superuser(username, password=DEMO_PASSWORD)

    def _create_demo_persons(self, count: int = 10):
        self.stdout.write(f"Adding {count} demo persons")
        for _ in range(count):
            gender = random.choice([GenderChoices.FEMALE, GenderChoices.MALE])
            first_names = MALE_FIRST_NAMES if gender == GenderChoices.MALE else FEMALE_FIRST_NAMES
            first_name = random.choice(first_names)
            last_name = random.choice(LAST_NAMES)
            date_of_birth = date(random.randint(1960, 2020), random.randint(1, 12), random.randint(1, 18))
            Person.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                date_of_birth=date_of_birth,
            )
