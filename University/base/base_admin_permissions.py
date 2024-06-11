'''
    Base classes for test if user is authenticated and
    the department have authorized access to admin functions.
    And display success messages
'''

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View

class BaseAdminUsers(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View
):
    '''
    Base class for test if user is authenticated and
    the department have authorized access to admin functions.
    And display success messages
    '''
    authorized_admin_access = [] # list for admin access

    def test_func(self):
        '''
        This function tests if authenticated user can access to this view
        '''

        if self.request.user.department in self.authorized_admin_access:
            return True

    def handle_no_permission(self):
        '''
        This function handles the no permission to access this view
        '''
        if self.raise_exception or self.request.user.is_authenticated:
            return redirect('index_manager')

        return redirect('login')

class BaseAdminUsersAdSe(BaseAdminUsers):
    '''
    Base class for test if user is authenticated and
    the department have authorized access to admin functions.
    And display success messages
    '''
    authorized_admin_access = ['ad', 'se']

class BaseAdminUsersAd(BaseAdminUsers):
    '''
    Base class for test if user is authenticated and
    the department have authorized access to admin functions.
    And display success messages
    '''
    authorized_admin_access = ['ad']

class BaseAdminUsersSe(BaseAdminUsers):
    '''
    Base class for test if user is authenticated and
    the department have authorized access to admin functions.
    And display success messages
    '''
    authorized_admin_access = ['se']

class BaseAdminUsersPr(BaseAdminUsers):
    '''
    Base class for test if user is authenticated and
    the department have authorized access to admin functions.
    And display success messages
    '''
    authorized_admin_access = ['pr']

    if __name__ == '__main__':
        pass