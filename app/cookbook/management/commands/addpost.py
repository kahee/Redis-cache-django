from django.core.management import BaseCommand

from cookbook.models import Book


class Command(BaseCommand):
    help = 'add as many posts as you want'

    def add_arguments(self, parser):
        parser.add_argument('post_cnt', type=int)

    def handle(self, *args, **options):
        post_cnt = options['post_cnt']
        if post_cnt > 0:
            Book.objects.bulk_create(
                [Book(text='Sample Text #{}'.format(i) for i in range(post_cnt))]
            )
            self.stdout.write(self.style.SUCCESS('Successfully add {} posts'.format(post_cnt)))