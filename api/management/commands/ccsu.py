from django.core.management import BaseCommand

from api.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--tg', type=str, help='Telegram ID')

    def handle(self, *args, **kwargs):
        email = 'admin@sky.pro'
        password = '123qwe'

        user = User.objects.create(
            email=email,
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password(password)
        user.save()
        print(f'email: {email}\npassword: {password}\n')
