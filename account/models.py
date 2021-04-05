from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(max_length=200,unique=True,verbose_name='ایمیل')
                             
    phone = models.CharField(max_length=12, unique=True, verbose_name='تلفن')
    Employee = models.BooleanField(default=False, verbose_name='آیا کارجو هستید؟')
    employer = models.BooleanField(default=False, verbose_name='آیا کارفرما هستید؟')
    avatar=models.ImageField(upload_to='avatars',verbose_name='تصویر شما',null=True,blank=True)
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")
    is_membership = models.DateTimeField(default=timezone.now,verbose_name='آکهی های ویژه')


    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت کاربر ویژه"


    def is_membership_user(self):
        if self.is_membership > timezone.now():
            return True
        else:
            return False

    is_membership_user.boolean = True
    is_membership_user.short_description = "وضعیت ثبت آگهی ویژه"
