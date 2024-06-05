"""
Models for User Account
- The username is the Email and not a name.
- The user is staff
- The user must belong to a department
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):

    DEPARTMENT_CHOICES = (
        ('AD', 'Administration'),
        ('FI', 'Finance'),
        ('SE', 'Secretary'),
        ('TE', 'Teacher'),
        ('ST', 'Student'),
        ('PA', 'Parent')
    )

    is_staff = models.BooleanField('Team member', default=True)
    department = models.CharField('Department', max_length=2, choices=DEPARTMENT_CHOICES, default='ST')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['first_name']

    def __str__(self):
        return self.username

    objects = UserManager()