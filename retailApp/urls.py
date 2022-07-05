from django.urls import path
from .views import upload_retail_csv,update_details

urlpatterns = [
    path('csv-data/',upload_retail_csv , name = 'csv-data'),
    path('update-detail/<str:pk>/', update_details, name="update-detail"),
]