from django.contrib.auth import views
from django.urls import path, include

from .views import EmployeeRegister,EmployerRegister,Profile

urlpatterns = [
    path('employee/register', EmployeeRegister.as_view(),name="employee-register"),
    path('employer/register', EmployerRegister.as_view(),name="employer-register"),
    path('login',views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    # path('dashboard', Dashboard.as_view(),name='home'),
    path('profile/', Profile.as_view(),name="profile"),
    # path('password_change/', passwordChange.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

