from django.contrib import admin
from .models import Jobs, Services, Cities, Category,massage

admin.site.register(Category)
admin.site.register(Cities)
admin.site.register(Services)
admin.site.register(Jobs)
admin.site.register(massage)
