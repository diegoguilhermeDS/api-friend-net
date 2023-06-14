from typing import Any, Optional
from django.core.management.base import CommandParser
from users.management.commands.names import first_names
from django.core.management import BaseCommand
from posts.models import Post
from users.models import User
from django.forms.models import model_to_dict


class Command(BaseCommand):
    help = "Creates an amount of posts for each user"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-qt",
            "--quantity",
            type=int,
            help="The ammount of posts for each user",
            default=5,
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        quantity = options["quantity"]

        for name in first_names:
            current_user = User.objects.get(username=name)
            current_user_dict = model_to_dict(current_user)

            for i in range(quantity):
                post_description = f"This is the {i} post from the user {current_user_dict['username']}"
                private = True
                if i % 2 == 0:
                    private = False
                Post.objects.create(
                    title=f"Título {i}",
                    description=post_description,
                    private=private,
                    published_by=current_user,
                )
        return_string = f"Created {quantity} posts for each users successufully"
        return self.stdout.write(self.style.SUCCESS(return_string))
