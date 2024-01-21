from django.core.management.base import BaseCommand
from tracker.utils.googlesheets import GoogleSheet
from tracker.models import Expense, Shop, Category
from django.contrib.auth.models import User

class Command(BaseCommand):
  help = 'Description of your command'

  def handle(self, *args, **options):
    x = User.objects.get(username='bo')
    shts = GoogleSheet()
    sheet_name = 'OUT'

    print('getting sheet contents...')
    shtsc = shts.get_sheet_contents(sheet_name)
    print('done!')

    print('processing sheet contents...')
    for i, row in enumerate(shtsc):
      print(f'processing row {i}...')

      description = row['description']
      category_name = row['category']
      shop_name = row['brand_shop']
      currency = row['currency']
      total = row['total']
      month = row['month']
      day = row['day']
      year = row['year']
      php = row['php']
      conversion = row['conversion']

      category, _created = Category.objects.get_or_create(
        name=category_name,
        created_by=x,
        updated_by=x,
      )
      if _created:
        print(f'new category {category.id} {category.name} created!')

      shop, _created = Shop.objects.get_or_create(
        name=shop_name,
        created_by=x,
        updated_by=x,
      )
      if _created:
        print(f'new shop {shop.id} {shop.name} created!')

      expense = Expense.objects.create(
        description=category_name,
        category=category,
        shop=shop,
        currency=currency,
        total=total,
        month=month,
        day=day,
        year=year,
        php=php,
        conversion=conversion,
        created_by=x,
        updated_by=x,
      )

      shts.write_to_sheet(sheet_name, f'A{i+2}', 'TEST')
      print(f'row A[{i}] saved!')

      if i == 10:
        break

      print('done!')
