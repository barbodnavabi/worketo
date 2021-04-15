from .views import JobCreate, JobListView,JobsDetailView,SearchjobsView,JobUpdate
from django.urls import path

urlpatterns = [
    path('job/create', JobCreate.as_view(), name='job-create'),
    path('jobs', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>', JobsDetailView.as_view(), name='job-detail'),
    path('job/update/<int:pk>', JobUpdate.as_view(), name='job-update'),
    path('job/search', SearchjobsView.as_view(), name='job-search'),
]
