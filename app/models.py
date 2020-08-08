from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from app.managers import CustomUserManager
from uuid import uuid4
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    real_name = models.CharField(max_length=30, verbose_name="first name")
    tz = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["real_name"]

    objects = CustomUserManager()

    class Meta:
        managed = True
        db_table = "app_users"

    def __str__(self):
        return self.real_name

    def get_username(self):
        return self.email

    def user_activity(self):
        user = self
        return ActivityPeriod.objects.filter(user=user)


class ActivityPeriod(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "activity_period"

