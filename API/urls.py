from django.urls import path
from .views import test_connection, data_series, handle_query, add_data, get_data, delete_data, get_data_notsorted

# these are usually the Django template paths.
# but for our purposes, these are the database API endpoints.

urlpatterns = [
    # urls for grafana
    path('', test_connection),
    path('search', data_series),
    path('query', handle_query),
 
    # urls for UDP
    path('addData', add_data), 
    path('getData', get_data),
    path('getDataNotSorted', get_data_notsorted),
    path('deleteALLData', delete_data)
]
