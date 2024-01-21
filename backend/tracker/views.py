from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.googlesheets import GoogleSheet
from .models import Expense

class SyncGoogleSheetsView(APIView):
  queryset = Expense.objects.all()

  def get(self, request):
    shts = GoogleSheet()
    return Response({
      "message": "Google Sheets sync completed.",
      'results': shts.get_all_sheets()})


class ProcessSheetView(APIView):
  queryset = Expense.objects.all()

  def get(self, request):
    shts = GoogleSheet()
    sheet_name = 'OUT'

    print('getting sheet contents...')
    shtsc = shts.get_sheet_contents(
      sheet_name
    )
    print('done!')

    print('processing sheet contents...')
    for i, row in enumerate(shtsc):
      print(f'processing row {i}...')
      print(row)
      print('done!')

    return Response({
      "message": f"Contents of sheet '{sheet_name}' read successfully.",
      "contents": shtsc})
