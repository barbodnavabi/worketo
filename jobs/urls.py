from .views import JobCreate, JobListView,JobsDetailView
from django.urls import path

urlpatterns = [
    path('job-create', JobCreate.as_view(), name='job-create'),
    path('jobs', JobListView.as_view(), name='job-view'),
    path('job/<int:pk>', JobsDetailView.as_view(), name='job-detail'),
]
