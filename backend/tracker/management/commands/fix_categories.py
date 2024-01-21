from django.core.management.base import BaseCommand

from core.models import Category, Expense

class Command(BaseCommand):
  help = 'process the tracker app'

  def handle(self, *args, **options):
    print('fixing categories...')

    category_list = list(Category.objects.all().values_list('name', flat=True))
    print(category_list)

    # # Find categories with more than 4 occurrences
    # categories_to_update = Category.objects.annotate(expense_count=Count('expense')).filter(expense_count__gt=4)

    # for category in categories_to_update:
    #     # Find expenses with the same shop name but no category
    #     expenses_to_update = Expense.objects.filter(shop=category.shop, category=None)

    #     # Update the expenses with the category that has more than 4 occurrences
    #     expenses_to_update.update(category=category)

    print('Categories fixed.')


