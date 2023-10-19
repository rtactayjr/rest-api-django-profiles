from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


# Create Models here

#  create custom user manager
class UserProfileManager(BaseUserManager):

    """Manager for user profiles"""

    """Create a new user profile"""
    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email) #1st half of the email are key-sensitive / 2nd half of email are all lowercase
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    """Create and save a new superuser with given details"""
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):

    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() # Calling class UserProfileManager - custom user manager

    # change the default field for logging in, from USERNAME to EMAIL
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email

from django.contrib.auth.models import BaseUserManager
...
