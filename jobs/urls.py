from .views import JobCreate, JobListView
from django.urls import path

urlpatterns = [
    path('job-create', JobCreate.as_view(), name='job-create'),
    path('jobs', JobListView.as_view(), name='job-view'),
]
