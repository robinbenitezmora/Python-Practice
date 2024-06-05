from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from accounts.models import CustomUser
from base.base_admin_permissions import BaseAdminUsersAdSe

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import (
    LoginView,
)

class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index-manager'))
        return super().get(request, *args, **kwargs)

class UserCreate(BaseAdminUsersAdSe, CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'accounts/user_new.html'
    success_url = reverse_lazy('index-manager')
    success_message = "User created successfully"

class UserChange(BaseAdminUsersAdSe, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/user-change.html'
    success_url = reverse_lazy('users')
    success_message = "User updated successfully"

class UserDelete(BaseAdminUsersAdSe, DeleteView):
    model = CustomUser
    template_name = 'accounts/user-delete.html'
    success_url = reverse_lazy('users')
    success_message = "User deleted successfully"

    def get_success_url(self):
        '''
        Only necessary for display success message after delete
        '''
        messages.success(self.request, self.success_message)

        return reverse('users')

class UserListView(BaseAdminUsersAdSe, ListView):
    model = CustomUser
    template_name = 'accounts/users.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return CustomUser.objects.all().order_by('first_name')