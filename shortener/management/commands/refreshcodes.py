from django.core.management.base import BaseCommand, CommandError

from shortener.models import LnrzURL


class Command(BaseCommand):
    help = 'Refrehes all LnrzURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return LnrzURL.objects.refresh_shortcodes(items=options['items'])