from django.core.management.base import NoArgsCommand
from django.conf import settings
from sms.models import SmsSender

class Command(NoArgsCommand):
    help = "Synchronize SmsSender"

    def handle_noargs(self, **options):
        SmsSender.synchronize()