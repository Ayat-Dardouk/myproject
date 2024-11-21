from django.urls import path
from . import views

urlpatterns = [
    path('upload-csv/', views.csv_to_excel, name='csv_to_excel'),
]
