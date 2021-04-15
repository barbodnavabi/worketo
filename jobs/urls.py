from .views import JobCreate, JobListView,JobsDetailView,SearchjobsView,JobUpdate,JobDelete
from django.urls import path

urlpatterns = [
    path('job/create', JobCreate.as_view(), name='job-create'),
    path('jobs', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>', JobsDetailView.as_view(), name='job-detail'),
    path('job/update/<int:pk>', JobUpdate.as_view(), name='job-update'),
    path('job/delete/<int:pk>', JobDelete.as_view(), name='job-delete'),
    path('job/search', SearchjobsView.as_view(), name='job-search'),
]
