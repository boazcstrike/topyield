from __future__ import print_function
import time
import cloudmersive_currency_api_client
from cloudmersive_currency_api_client.rest import ApiException
from pprint import pprint

from django.conf import settings

class CloudMersiveAPI:
  def __init__(self):
    self.api_key = settings.CLOUDMERSIVE_API_KEY

  def get_available_currencies(self):
    configuration = cloudmersive_currency_api_client.Configuration()
    configuration.api_key['Apikey'] = self.api_key

    # create an instance of the API class
    api_instance = cloudmersive_currency_api_client.CurrencyExchangeApi(cloudmersive_currency_api_client.ApiClient(configuration))

    try:
      # Get a list of available currencies and corresponding countries
      api_response = api_instance.currency_exchange_get_available_currencies()
      return api_response.to_dict()
    except ApiException as e:
      print("Exception when calling CurrencyExchangeApi->currency_exchange_get_available_currencies: %s\n" % e)
