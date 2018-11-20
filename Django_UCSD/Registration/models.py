from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core import validators


# This App has no models


class AccountManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError('You must have an email address to register ')
        account = self.model(
            email=self.normalize_email(email),
            # password=password
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password):
        account = self.model(
            email=self.normalize_email(email),
            # password=password
        )
        account.set_password(password)
        account.is_admin = True
        account.save()
        return account


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # password = models.CharField(max_length=30, validators=[validators.MinLengthValidator(8, message='Password must be at least 8 characters!')])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
