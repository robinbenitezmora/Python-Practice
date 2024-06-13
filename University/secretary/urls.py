from django.urls import path
from secretary.views import (
    IndexSecretaryView,
    SecretarySearchView,
)

urlpatterns = [
    path('', IndexSecretaryView.as_view(), name='index_secretary'),
    path('search/', SecretarySearchView.as_view(), name='search_secretary')
]