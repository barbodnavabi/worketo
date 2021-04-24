from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from .forms import  SignupForm,ProfileForm
from .models import User
from django.contrib.auth.views import PasswordChangeView
from jobs.models import Jobs
from jobs.mixins import UserAccessMixin

class Dashboard(UserAccessMixin,LoginRequiredMixin, ListView):
    template_name = 'registration/dashboard.html'
    paginate_by= 8

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Jobs.objects.all()
        else:
            return Jobs.objects.filter(author=self.request.user)


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("profile")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwags = super(Profile, self).get_form_kwargs()
        kwags.update({
            'user': self.request.user
        })
        return kwags


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    template_name='registration/password_change.html'


class EmployeeRegister(CreateView):
    model = User
    form_class = SignupForm
    template_name = "registration/signup_employee.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.Employee = True
        form.save()
        return super().form_valid(form)


class EmployerRegister(CreateView):
    model = User
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.employer = True
        form.save()
        return super().form_valid(form)
