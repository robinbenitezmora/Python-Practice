from django.urls import path
from teachers.views import (
	IndexTeacherView
)


urlpatterns = [
	path('', IndexTeacherView.as_view(), name='index_teacher')
]
