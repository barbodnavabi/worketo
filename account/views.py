from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from .forms import  SignupForm
from .models import User


# class Dashboard(LoginRequiredMixin, ListView):
#     template_name = 'AdminLTE/home.html'
#     context_object_name = 'listing'
#     paginate_by = 16

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return Listing.objects.all()
#         else:
#             return Listing.objects.filter(author=self.request.user)


# class Profile(LoginRequiredMixin, UpdateView):
#     model = User
#     template_name = 'AdminLTE/profile.html'
#     form_class = ProfileForm
#     success_url = reverse_lazy("profile")

#     def get_object(self):
#         return User.objects.get(pk=self.request.user.pk)

#     def get_form_kwargs(self):
#         kwags = super(Profile, self).get_form_kwargs()
#         kwags.update({
#             'user': self.request.user
#         })
#         return kwags


# class passwordChange(PasswordChangeView):
#     success_url = reverse_lazy('password_change_done')


class EmployeeRegister(CreateView):
    model = User
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.Employee = True
        form.save()
        return super().form_valid(form)

# class Register(CreateView):
#     model = User
#     form_class = SignupForm
#     template_name = "registration/register.html"
#     success_url = reverse_lazy('login')

