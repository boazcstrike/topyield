from django.contrib import admin
from django.urls import path
from tracker.views import SyncGoogleSheetsView, ProcessSheetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sync-google-sheets/', SyncGoogleSheetsView.as_view(), name='sync-google-sheets'),
    path('process-assets-expenses/', ProcessSheetView.as_view(), name='process-assets-expenses'),
]
