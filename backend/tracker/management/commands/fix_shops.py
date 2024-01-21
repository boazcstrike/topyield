import pprint
from django.core.management.base import BaseCommand
from django.db.models import Count

from core.utils.main import is_name_similar
from tracker.models import Shop


class Command(BaseCommand):
  help = 'process the tracker app'


  def handle(self, *args, **options):
    print('fixing shops...')
    print('cleaning dupes...')
    duplicate_names = Shop.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

    for duplicate in duplicate_names:
      name = duplicate['name']
      instances_to_delete = Shop.objects.filter(name=name)
      instance_to_keep = instances_to_delete.order_by('id').first()
      instances_to_delete = instances_to_delete.exclude(pk=instance_to_keep.pk)
      for instance in instances_to_delete:
        instance.expense_shop.all().update(shop=instance_to_keep)
      instances_to_delete.delete()

    print('done cleaning dupes')

    shop_list = Shop.objects.values_list('name', flat=True)
    print('counting the occurrences of each shop')
    shop_counts = {}
    for shop in shop_list:
      shop_counts[shop] = shop_counts.get(shop, 0) + 1

    print('finding the main shops with more repeated values')
    main_shops = []
    for shop in shop_list:
      pprint.pprint(is_name_similar(shop, shop_list), indent=2)



