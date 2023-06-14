from users.models import User
from django.forms.models import model_to_dict
from django.core.management import BaseCommand
from django.core.management.base import CommandParser, CommandError
from django.db.models import Q


class Command(BaseCommand):
    help = "Creates an admin user"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="The username for the admin account",
            default="admin",
        )
        parser.add_argument(
            "-e",
            "--email",
            type=str,
            help="The email for the admin account",
            default="admin@mail.com",
        )
        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="The password for the admin account",
            default="admin1234",
        )

    def handle(self, *args, **options: dict) -> str | None:
        username = options["username"]
        email = options["email"]
        password = options["password"]

        try:
            user_db = User.objects.get(Q(username=username) | Q(email=email))
            user_db = model_to_dict(user_db)
        except User.DoesNotExist:
            User.objects.create_superuser(
                username=username, email=email, is_superuser=True, password=password
            )
            return_string = f"Admin `{username}` successfully created!"
            return self.stdout.write(self.style.SUCCESS(return_string))

        if user_db["username"] == username:
            raise CommandError(f"Username `{username}` already taken.")
        raise CommandError(f"Email `{email}` already taken.")
