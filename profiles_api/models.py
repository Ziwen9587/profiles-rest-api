from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermssionsMixin

# Create your models here.
class UserProfile(AbstractBaseUser,PermssionsMixin):
    """Database model for users in the system
    """
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    # this is a django custom model manager
    # UserProfileManager class will be created in future video
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'name' ]

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """String representation of user"""
        return self.email
