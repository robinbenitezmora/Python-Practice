'''
schoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('webpage.urls')),
    path('users/', include('accounts.urls')),
    path('administration/', include('administration.urls')),
    path('students/', include('students.urls')),
    path('finance/', include('finance.urls')),
    path('principal/', include('principal.urls')),
    path('teachers/', include('teachers.urls')),
    path('parents/', include('parents.urls')),
    path('secretary/', include('secretary.urls')),
    path('classes/', include('classes.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Django Debug toolbar, only in development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

    handler403 = 'webpage.views.error_403'
    handler404 = 'webpage.views.error_404'
    handler500 = 'webpage.views.error_500'