from django.urls import path
from administration.views import (
    IndexAdminstrationView,
    AdministrationSearchView,
)

urlpatterns = [
    path('', IndexAdminstrationView.as_view(), name='index-administration'),
    path('search/', AdministrationSearchView.as_view(), name='search-administration'),
]
