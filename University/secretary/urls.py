from django.urls import path
from secretary.views import (
    IndexSecretaryView
)

urlpatterns = [
    path('', IndexSecretaryView.as_view(), name='index_secretary')
]