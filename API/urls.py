from django.urls import path
from .views import test_connection, add_data, get_data, delete_data

# these are usually the Django template paths.
# but for our purposes, these are the database API endpoints.

urlpatterns = [
  path('', test_connection),
  path('addData', add_data),
  path('getData', get_data),
  path('deleteALLData', delete_data)
]