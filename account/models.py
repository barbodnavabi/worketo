from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(max_length=200,unique=True,verbose_name='ایمیل') 
    phone = models.PositiveIntegerField(verbose_name='تلفن')
    address = models.TextField(verbose_name='آدرس')
    bio = models.TextField(verbose_name='توضیحات و بیوگرافی شما')
    github=models.URLField(verbose_name='لینک گیتهاب',null=True,blank=True)
    linkendin=models.URLField(verbose_name='لینکندین',null=True,blank=True)
    website=models.URLField(verbose_name='وبسایت شما',null=True,blank=True)
    facebook=models.URLField(verbose_name='لینک فیسبوک',null=True,blank=True)
    instagram=models.URLField(verbose_name='لینک اینستاگرام',null=True,blank=True)
    telegram=models.URLField(verbose_name='تلگرام',null=True,blank=True)
    whatsApp=models.CharField(verbose_name='واتساپ',null=True,blank=True,max_length=50)
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
