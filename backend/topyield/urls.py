from django.contrib import admin
from django.urls import path
from tracker.views import SyncGoogleSheetsView, ProcessSheetView
from fengshui.views import FengShuiReadingView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sync-google-sheets/', SyncGoogleSheetsView.as_view(), name='sync-google-sheets'),
    path('process-assets-expenses/', ProcessSheetView.as_view(), name='process-assets-expenses'),
    path('api/fengshui/', FengShuiReadingView.as_view(), name='fengshui'),
]
