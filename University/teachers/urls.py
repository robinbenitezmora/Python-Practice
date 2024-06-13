from django.urls import path
from teachers.views import (
				TeacherListView,
				IndexTeacherView,
				TeacherNewView,
				TeacherUpdateView,
				TeacherDeleteView,
)

urlpatterns = [
				path('teachers/', TeacherListView.as_view(), name='teachers'),
				path('', IndexTeacherView.as_view(), name='index_teacher'),
				path('teachers_new/', TeacherNewView.as_view(), name='new_teacher'),
				path('<int:pk>/change', TeacherUpdateView.as_view(), name='change_teacher'),
				path('<int:pk>/delete', TeacherDeleteView.as_view(), name='delete_teacher'),
]
