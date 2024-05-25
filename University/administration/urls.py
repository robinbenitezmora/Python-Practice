from django.urls import path
from administration.views import (
    IndexAdminstrationView
)

urlpatterns = [
    path('', IndexAdminstrationView.as_view(), name='index-administration'),
]
