import gspread
from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials
from decimal import Decimal, InvalidOperation

class GoogleSheet:
  """
  Represents a Google Sheet and provides methods for interacting with it.
  """

  def __init__(self):
    self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1rfS0yAGhWra8Kcc4a_phlaYZqRPs7OuYWbvb2etsJVw/'

  @staticmethod
  def connect_to_google_sheets():
    """
    Connects to Google Sheets using the provided credentials and returns the authorized client.

    Returns:
      gspread.Client: The authorized client for accessing Google Sheets.
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_CREDENTIAL_JSON_FILE, scope)
    client = gspread.authorize(credentials)
    return client

  def handle_exceptions(self, e):
    if isinstance(e, gspread.exceptions.APIError) or isinstance(e, PermissionError):
      print(f"{type(e).__name__}: {e}")
    else:
      print(f"An unexpected error occurred: {e}")

  def get_all_sheets(self) -> list:
    """
    Retrieves the names of all sheets in the Google Sheet.

    Returns:
      list: A list of sheet names.
    """
    try:
      gc = GoogleSheet.connect_to_google_sheets()
      spreadsheet = gc.open_by_url(self.spreadsheet_url)
      sheets = spreadsheet.worksheets()
      sheet_names = [sheet.title for sheet in sheets]
      return sheet_names
    except Exception as e:
      self.handle_exceptions(e)

  def get_sheet_contents(self, sheet_name: str) -> list:
    """
    Retrieves the contents of a sheet in the Google Sheet.

    Args:
      sheet_name (str): The name of the sheet to retrieve the contents of.

    Returns:
      list: A list of dictionaries representing the contents of the sheet.
    """
    try:
      gc = GoogleSheet.connect_to_google_sheets()
      spreadsheet = gc.open_by_url(self.spreadsheet_url)
      worksheet = spreadsheet.worksheet(sheet_name)
      data = worksheet.get_all_records()
      return data
    except Exception as e:
      self.handle_exceptions(e)

  def write_to_sheet(self, sheet_name: str, cell: str, content: str):
    """
    Writes data to a sheet in the Google Sheet.

    Args:
      sheet_name (str): The name of the sheet to write the data to.
      data (list): The data to write to the sheet.
    """
    try:
      gc = GoogleSheet.connect_to_google_sheets()
      spreadsheet = gc.open_by_url(self.spreadsheet_url)
      worksheet = spreadsheet.worksheet(sheet_name)
      worksheet.update(cell, content)
    except Exception as e:
      self.handle_exceptions(e)

  def convert_to_positive_decimal(self, value):
    """
    Checks if the value is a float and converts it to a positive decimal if it's negative.

    Args:
      value: The value to check and convert.

    Returns:
      decimal.Decimal: The converted positive decimal value.
    """
    if isinstance(value, float):
      if value < 0:
        value = abs(value)

    if isinstance(value, str):
      if value.startswith("(") and value.endswith(")"):
        value = value[1:-1]

    try:
        return Decimal(value)
    except InvalidOperation:
        print(f"Invalid value: {value}")

  def test(self):
    """
    Performs a test operation on the Google Sheet.
    """
    try:
      gc = GoogleSheet.connect_to_google_sheets()
      worksheet = gc.open_by_url(self.spreadsheet_url).sheet1
      print(worksheet)
      data = worksheet.get_all_records()
      print(data)
    except Exception as e:
      self.handle_exceptions(e)
