from django.urls import path
from .views import test_connection, data_series, add_data, get_data, delete_data

# these are usually the Django template paths.
# but for our purposes, these are the database API endpoints.

urlpatterns = [
    # urls for grafana
    path('', test_connection),
    path('search', data_series),

    # urls for UDP
    path('addData', add_data),
    path('getData', get_data),
    path('deleteALLData', delete_data)
]
