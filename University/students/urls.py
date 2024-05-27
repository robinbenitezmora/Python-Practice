from django.urls import path
from students.views import (
    StudentIndexView,
    StudentNewView
)

urlpatterns = [
    path('', StudentIndexView.as_view(), name='index_student'),
    path('new_student/', StudentNewView.as_view(), name='new_student')
]
