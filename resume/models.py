from django.db import models
from django.conf import settings
# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=200,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(("ایمیل"), max_length=254,blank=True,null=True)
    phone = models.PositiveIntegerField(verbose_name='تلفن')
    image = models.ImageField(upload_to='images',verbose_name='تصویر شما',null=True,blank=True)
    address = models.TextField(verbose_name='آدرس')
    bio = models.TextField(verbose_name='توضیحات و بیوگرافی شما')
    github = models.URLField(verbose_name='لینک گیتهاب',null=True,blank=True)
    linkendin = models.URLField(verbose_name='لینکندین',null=True,blank=True)
    website = models.URLField(verbose_name='وبسایت شما',null=True,blank=True)
    facebook = models.URLField(verbose_name='لینک فیسبوک',null=True,blank=True)
    instagram = models.URLField(verbose_name='لینک اینستاگرام',null=True,blank=True)
    telegram = models.URLField(verbose_name='تلگرام',null=True,blank=True)
    whatsApp = models.PositiveIntegerField(verbose_name='واتساپ',null=True,blank=True)

    def __str__(self):
        return self.user.username
class Study(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    description=models.TextField(verbose_name='توضیحات',blank=True,null=True)
    course = models.CharField(max_length=200,verbose_name='مهارت')
    college = models.CharField(max_length=300,verbose_name='دانشکده')


    def __str__(self):
        return self.description


class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    skill = models.CharField(max_length=50, null=True, blank=True,verbose_name='مهارت')
    percent = models.DecimalField(max_digits=4, decimal_places=0,verbose_name='چند درصد در این مهارت حرفه ای هستید؟')

    def __str__(self):
        return self.user.username



class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, null=True, blank=True,verbose_name='نام پروژه')
    description = models.TextField(("نقش شما در پروژه"))
    type = models.CharField(max_length=50, null=True, blank=True,verbose_name='زمینه کاری پروژه')
    link = models.CharField(max_length=2084, null=True, blank=True,verbose_name='لینک پروژه')
    date_created = models.DateField(("date_created"),auto_now_add=True)
    image = models.ImageField(upload_to="projects",blank=True,null=True,verbose_name='عکس')

    def __str__(self):
        return self.user.username


class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    organisation_name = models.CharField(max_length=50, null=True, blank=True,verbose_name='نام شرکت یا سازمان')
    post = models.CharField(max_length=50, null=True, blank=True,verbose_name='مقام شما در شرکت')
    joining_date = models.DateField(verbose_name='تاریخ عضویت')
    ending_date = models.DateField( blank=True, null=True,verbose_name='تاریخ پایان کاری')
    work_experience = models.TextField(verbose_name='توضیحات کاری',blank=True,null=True)

    def __str__(self):
        return self.user.username