from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Creates super user during project start up'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': '',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('admin')
            user.save()

        print(f'Superuser with {user.username} {"created" if created else "already exists"}')
