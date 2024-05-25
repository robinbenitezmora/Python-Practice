"""
Models for User Account
- The username is the Email and not a name.
- The user is staff
- The user must belong to a department
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields, username=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):

    DEPARTMENT_CHOICES = (
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('AC', 'Accounting'),
        ('SA', 'Sales'),
        ('MA', 'Marketing'),
        ('PR', 'Production'),
        ('LO', 'Logistics'),
        ('PU', 'Purchasing'),
    )

    email = models.EmailField('Email', unique=True)
    is_staff = models.BooleanField('Staff Status', default=True)
    department = models.CharField(
        'Department',
         max_length=2,
         choices=DEPARTMENT_CHOICES
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'department']

    def __str__(self):
        return self.email

    objects = CustomUserManager()