from django.urls import path
from parents.views import (
    IndexParentView
)

urlpatterns = [
    path('', IndexParentView.as_view(), name='index_parent')
]