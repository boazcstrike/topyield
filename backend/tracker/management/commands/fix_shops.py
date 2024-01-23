import json
import pprint
from django.core.management.base import BaseCommand
from django.db.models import Count

from core.utils.main import is_name_similar
from tracker.models import Shop


class Command(BaseCommand):
  help = 'process the tracker app'

  def get_unique_values(self, arr: list) -> list:
    unique_values = set()
    for sublist in arr:
        for dictionary in sublist:
            for key, value_dict in dictionary.items():
                unique_values.add(key)
                for value in value_dict.keys():
                    unique_values.add(value)
    print(list(unique_values))
    return list(unique_values)

  def map_decision(self, shop_similarities: list) -> list:
    decision_map = []
    for shop in shop_similarities:
      decision = input(f'keep {shop}? (y/n)')
      while decision != 'y' or decision != 'n':
        if decision == 'y':
          decision_map.append({shop: True})
        elif decision == 'n':
          decision_map.append({shop: False})
        else:
          decision_map.append({shop: True})
    print(decision_map)
    return decision_map

  def execute_decision(self, decision_map: list):
    for decision in decision_map:
      for shop, keep in decision.items():
        if keep:
          print(f'keeping {shop}')
        else:
          print(f'deleting {shop}')

  def process_cleaning(self, shop_similarities):
    shop_similarities = self.get_unique_values(shop_similarities)
    decision_map = self.map_decision(shop_similarities)
    self.execute_decision(decision_map)

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

    print('starting cleaning process...')

    for shop in shop_list:
      shop_similarities = is_name_similar(shop, shop_list)
      if shop_similarities:
        pprint.pprint(json.dumps(shop_similarities, indent=2))
        self.process_cleaning(shop_similarities)
        break





