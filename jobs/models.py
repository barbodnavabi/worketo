from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from account.models import User


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name="زیردسته")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    objects = CategoryManager()

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/categories/{self.slug}'


class CityManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Cities(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name="زیردسته")
    title = models.CharField(max_length=200, verbose_name="نام استان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس استان")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    objects = CityManager()

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/categories/{self.slug}'


class Services(TaggedItemBase):
    content_object = models.ForeignKey('JObs', on_delete=models.CASCADE,related_name='services')


Job_CHOICES = [
    ('دور کاری', 'دور کاری'),
    ('تمام وقت', 'تمام وقت'),
    ('پاره وقت', 'پاره وقت'),
    ('کارآموزی', 'کارآموزی'),
    ('پروژه ای', 'پروژه ای'),

]
STATUS_CHOICES = (
    ('p', "منتشر شده"),
    ('i', "در حال بررسی"),
    ('b', "منقضی شده"),
)
SOLDIER_CHOICES = (
    ('معاف', "معاف"),
    ('پایان خدمت', "پایان خدمت"),
    ('مهم نیست', "مهم نیست"),
)
EXPERIANCE_CHOICES = (
    ('جونیور', "جونیور"),
    ('سنیور', "سنیور"),
    ('مید لول', "مید لول"),
    ('مهم نیست', "مهم نیست"),
)

PRICE_CHOICES = (
    ('توافقی', "توافقی"),
    ('2 تا 3 میلیون', "2 تا 3 میلیون"),
    ('8 تا 9 میلیون', "8 تا 9 میلیون"),
    ('10 تا 12 میلیون', "10 تا 12 میلیون"),
    ('12 تا 20 میلیون' , "12 تا 20 میلیون"),
    ('دیگر قیمت ها', "دیگر قیمت ها"),
)

SEX_CHOICES = (
    ('مرد', "مرد"),
    ('زن', "زن"),
    ('مهم نیست', "مهم نیست"),
   

)

class Jobs(models.Model):
    author = models.ForeignKey(User, models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=300, verbose_name='عنوان شغلی')
    company = models.CharField(max_length=300, verbose_name='نام شرکت')
    description = models.TextField(verbose_name='توضیحات شغلی')
    employer_description = models.TextField(verbose_name='نفش کارمند در شرکت')
    address = models.TextField(verbose_name='آدرس شرکت شما')
    important = TaggableManager(blank=True, verbose_name='مهارت های لازم')
    service = TaggableManager(through=Services,blank=True, verbose_name='مسئولیت ها',related_name='services')
    price = models.CharField(max_length=200, default='12 تا 20 میلیون', choices=PRICE_CHOICES, verbose_name="حقوق")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='دسته بندی', blank=True, null=True)
    state = models.ForeignKey(Cities, on_delete=models.SET_NULL, verbose_name='شهر', blank=True, null=True)
    Type = models.CharField(max_length=200, default='d', choices=Job_CHOICES, verbose_name="وضعیت شغلی")
    status = models.CharField(max_length=200, default='i', choices=STATUS_CHOICES, verbose_name="وضعیت")
    soldiering = models.CharField(max_length=200, default='مهم نیست', choices=SOLDIER_CHOICES,
                                  verbose_name="وضعیت نظام وظیفه")
    sex = models.CharField(max_length=200, default='مهم نیست', choices=SEX_CHOICES,
                                  verbose_name="جنسیت")   
    experiance = models.CharField(max_length=200, default='مهم نیست', choices=EXPERIANCE_CHOICES,
                                  verbose_name="سطح تجربه")   
    date=models.DateTimeField(auto_now_add=True,verbose_name='زمان ثبت')                                                       

    def __str__(self):
        return self.company






class massage(models.Model):
    name=models.CharField(max_length=300,verbose_name='نام')
    pdf=models.FileField(upload_to='pdf',verbose_name='فایل رزومه')
    phone=models.CharField(max_length=300,verbose_name='تلفن')
    email=models.EmailField(("ایمیل"), max_length=254,blank=True,null=True)
    revicer=models.ForeignKey(User, verbose_name=('دریافت کننده'), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    