from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AnonymousUser as DjangoAnonymousUser
import uuid
from django.core import validators
#from User.models import UserProfile
from django.db.models.signals import post_save
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

    account_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    last_searched_keyword = models.CharField(max_length=1000, default=None, null=True, blank=True)
    #user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # password = models.CharField(max_length=30, validators=[validators.MinLengthValidator(8, message='Password must be at least 8 characters!')])
    is_new_user = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.user.__str__()

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

    def set_new_user(self):
        self.is_new_user = False
        self.save()

    def save_keyword(self, keyword):
        self.last_searched_keyword = keyword
        self.save()

    def erase_keyword(self):
        self.last_searched_keyword = None
        self.save()

    def get_keyword(self):
        return self.last_searched_keyword


class Anonymous(AbstractBaseUser):
    ip = models.CharField(max_length=200, unique=True)
    last_searched_keyword = models.CharField(max_length=1000, default=None, null=True, blank=True)
    is_staff = False
    is_active = False
    is_superuser = False

    USERNAME_FIELD = 'ip'
    REQUIRED_FIELDS = ['ip']

    def __init__(self, request):
        self.ip = request.META.get('REMOTE_ADDR')

    def __str__(self):
        return '灭霸'

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1  # instances always return the same hash value

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_authenticated(self):
        return False

    def get_ip(self):
        return self.ip

    def save_keyword(self, keyword):
        self.last_searched_keyword = keyword
        self.save()

    def erase_keyword(self):
        self.last_searched_keyword = None
        self.save()

    def get_keyword(self):
        return self.last_searched_keyword
