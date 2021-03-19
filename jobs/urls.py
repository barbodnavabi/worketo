from .views import JobCreate
from django.urls import path

urlpatterns = [
    path('job-create', JobCreate.as_view(), name='job-create'),
]
