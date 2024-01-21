from django.core.management.base import BaseCommand
from tracker.models import WorldCurrency
from django.contrib.auth.models import User
from tracker.utils.cloudmersive import CloudMersiveAPI

class Command(BaseCommand):
  help = 'syncs the currency list from an API - cloudmersive'

  def handle(self, *args, **options):
    cm = CloudMersiveAPI()
    response = cm.get_available_currencies()
    currencies = response['currencies']

    for currency in currencies:
      name = currency['country_name'] + ' ' + currency['currency_english_name']
      symbol = currency['currency_symbol']
      code = currency['iso_currency_code']
      WorldCurrency.objects.get_or_create(
        name=name,
        symbol=symbol,
        code=code,
      )
      print(f'new currency {name} {symbol} {code} created!')