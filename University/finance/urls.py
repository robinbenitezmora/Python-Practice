from django.urls import path
from finance.views import (
    IndexFinanceView
)

urlpatterns = [
    path('', IndexFinanceView.as_view(), name='index_finance')
]