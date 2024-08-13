import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from table.models import TableEntry


class Command(BaseCommand):
    help = 'Generate random table data'

    def handle(self, *args, **kwargs):
        for obj in range(1000):
            TableEntry.objects.create(
                date=datetime.now() - timedelta(days=random.randint(0, 100)),
                name=f'Object with name: {random.randint(1, 100)}',
                quantity=random.randint(1, 1000),
                distance=random.uniform(1.0, 1000.0)
            )
        self.stdout.write(self.style.SUCCESS('Successfully generated random data'))
