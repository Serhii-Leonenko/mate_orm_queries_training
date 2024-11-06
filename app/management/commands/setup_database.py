from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Sets up the database by applying migrations and loading fixture data.'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write("Applying migrations...")
            call_command("migrate")

            self.stdout.write("Loading fixture data...")
            call_command("loaddata", "fixture.json")

            self.stdout.write(self.style.SUCCESS("Database setup complete."))
        except CommandError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
