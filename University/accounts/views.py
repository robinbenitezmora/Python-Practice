from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import CustomUser
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

class UserCreate(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'accounts/user-new.html'
    success_url = 'accounts/login/'
    success_message = 'Welcome! Log in to get started'

class UserChange(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/user-change.html'
    success_url = '/'
    success_message = 'Your profile has been successfully changed'

    def get_queryset(self):

        if self.request.user.is_authenticated:
            return self.model.objects.filter(username=self.request.user)
        else:
            return super().get_queryset().filter(username=None)

class UserDelete(SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'accounts/user-delete.html'
    success_url = '/'
    success_message = 'Your profile has been successfully deleted'

    def get_queryset(self):

        if self.request.user.is_authenticated:
            return self.model.objects.filter(username=self.request.user)
        else:
            return super().get_queryset().filter(username=None)

class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = '/'
    success_message = 'Your password has been successfully changed'

class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'
    success_url = '/'
    success_message = 'A password reset link has been sent to your email'

class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_message = 'Your password has been successfully reset'

class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
    success_url = '/'
    success_message = 'Your password has been changed correctly. Log in to get started'