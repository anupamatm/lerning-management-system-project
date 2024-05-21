# lms_admin/management/commands/create_lms_admin.py

from django.core.management.base import BaseCommand
from authentication.models import CustomUser
from lms_admin.models import LmsAdmin

class Command(BaseCommand):
    help = 'Create an LmsAdmin user'

    def handle(self, *args, **kwargs):
        if not CustomUser.objects.filter(username='lamsadmin').exists():
            user = CustomUser.objects.create_superuser(
                username='lamsadmin',
                password='12345',
                user_type='admin'
            )
            LmsAdmin.objects.create(user=user, username=user.username, password='12345')
            self.stdout.write(self.style.SUCCESS('Successfully created LmsAdmin user'))
        else:
            self.stdout.write(self.style.WARNING('LmsAdmin user already exists'))
