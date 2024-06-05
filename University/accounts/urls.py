from django.urls import path, include
from accounts.views import (
    UserLogin,
				UserCreate,
				UserChange,
				UserDelete,
				UserListView,
)

urlpatterns = [
				path('login/', UserLogin.as_view(), name='login'),
				path('users/', UserListView.as_view(), name='users'),
				path('user-new/', UserCreate.as_view(), name='user-new'),
				path('<int:pk>/update', UserChange.as_view(), name='user-change'),
				path('<int:pk>/delete', UserDelete.as_view(), name='user-delete'),
				path('', include('django.contrib.auth.urls')),
]
				


