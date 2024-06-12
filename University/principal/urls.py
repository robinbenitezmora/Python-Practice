from django.urls import path
from principal.views import (
    DisciplineListView,
    DisciplineNewView,
    DisciplineUpdateView,
)

urlpatterns = [
    path('disciplines/', DisciplineListView.as_view(), name='disciplines'),
    path('disciplines/new/', DisciplineNewView.as_view(), name='discipline_new'),
    path('<int:pk>/change/', DisciplineUpdateView.as_view(), name='discipline_update'),
]