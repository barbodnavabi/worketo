from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=12, unique=True, verbose_name='تلفن')
    Employee = models.BooleanField(default=False, verbose_name='آیا کارجو هستید؟')
    employer = models.BooleanField(default=False, verbose_name='آیا کارفرما هستید؟')
