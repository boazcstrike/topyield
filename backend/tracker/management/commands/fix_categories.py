from django.core.management.base import BaseCommand

from core.utils.main import is_name_similar
from core.models import Category

class Command(BaseCommand):
  help = 'process the tracker app'

  def handle(self, *args, **options):
    print('fixing categories...')

    category_list = list(Category.objects.all().values_list('name', flat=True))
    print(category_list)

    # Count the occurrences of each category
    category_counts = {}
    for category in category_list:
      category_counts[category] = category_counts.get(category, 0) + 1

    # Find the main categories with more repeated values
    main_categories = []
    for category, count in category_counts.items():
      if count > len(category_list) / 2:
        main_categories.append(category)

    # Find the less repeated categories
    less_repeated_categories = []
    for category, count in category_counts.items():
      if count < len(category_list) / 2:
        less_repeated_categories.append(category)

    # Add the less repeated categories to the list of words that can be included with the main categories
    words_to_include = main_categories + less_repeated_categories

    print(f'Main categories: {main_categories}')
    print(f'Less repeated categories: {less_repeated_categories}')
    print(f'Words to include: {words_to_include}')

    for category in category_list:
      category_list_wo_selected_category = [category for category in category_list if category != 'category']
      if is_name_similar(category, category_list_wo_selected_category):
        print(f'category {category} is similar to another category')
