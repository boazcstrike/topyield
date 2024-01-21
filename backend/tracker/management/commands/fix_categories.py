from django.core.management.base import BaseCommand

from core.utils.main import is_name_similar
from core.models import Category

class Command(BaseCommand):
  help = 'process the tracker app'

  def handle(self, *args, **options):
    print('fixing categories...')

    category_list = list(Category.objects.all().values_list('name', flat=True))
    print(category_list)

