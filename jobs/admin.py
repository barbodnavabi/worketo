from django.contrib import admin

# Register your models here.
from jobs.models import Jobs, Services, Cities, Category

admin.site.register(Category)
admin.site.register(Cities)
admin.site.register(Services)
admin.site.register(Jobs)
