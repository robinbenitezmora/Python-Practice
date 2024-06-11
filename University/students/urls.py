from django.urls import path
from students.views import (
    StudentIndexView,
    StudentNewView,
    StudentListView,
    StudentEfectiveView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path('', StudentIndexView.as_view(), name='index_student'),
    path('students/', StudentListView.as_view(), name='students'),
    path('students/new/', StudentNewView.as_view(), name='new_student'),
    path('students/efective/', StudentEfectiveView.as_view(), name='efective_student'),
    path('<int:pk>change/', StudentUpdateView.as_view(), name='student_change'),
    path('<int:pk>delete/', StudentDeleteView.as_view(), name='student_delete'),
]
