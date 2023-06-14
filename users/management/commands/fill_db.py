from typing import Any, Optional
from django.core.management import BaseCommand
from django.core.management.base import CommandParser, CommandError
from .names import first_names, last_names
from users.models import User
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Creates 10 users to populate the database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        try:
            for i in range(len(first_names)):
                current_user = User.objects.create(
                    username=first_names[i].lower(),
                    first_name=first_names[i],
                    last_name=last_names[i],
                    email=f"{first_names[i].lower()}@mail.com",
                )
                current_user.set_password("1234")
                current_user.save()
            return_string = f"Created 10 users successufully"
            return self.stdout.write(self.style.SUCCESS(return_string))
        except IntegrityError as e:
            print("Users already registered")
