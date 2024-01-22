from django.core.management.base import BaseCommand
from tracker.utils.googlesheets import GoogleSheet
from tracker.models import Expense, Shop, Category, WorldCurrency
from django.contrib.auth.models import User
from decimal import Decimal

class Command(BaseCommand):
  help = 'process the tracker app'

  def handle(self, *args, **options):
    x = User.objects.get(username='bo')
    shts = GoogleSheet()
    sheet_name = 'OUT'

    print('getting sheet contents...')
    shtsc = shts.get_sheet_contents(sheet_name)

    print('processing sheet contents...')
    for i, row in enumerate(shtsc):
      print(f'processing row [{i}]...')

      description = row['description']
      category_name = row['category']
      shop_name = row['brand_shop']
      currency = row['currency']

      total = row['total']
      php = row['php']
      month = row['month']
      day = row['day']
      year = row['year']
      conversion = row['conversion']

      if month == '':
        month = None
      if day == '':
        day = None
      if year == '':
        year = None

      total = shts.convert_to_positive_decimal(total)
      php = shts.convert_to_positive_decimal(php)

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

      currency = WorldCurrency.objects.get(code=currency)

      expense = Expense.objects.create(
        description=description,
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
        cell=f'A{i+2}',
      )
      print(f'expense {currency.name} {expense.total} recorded')

      shts.write_to_sheet(sheet_name, f'A{i+2}', i)
      print(f'row A[{i+2}] saved!\n')

