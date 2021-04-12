from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from jobs.mixins import FormValidMixin
from jobs.models import Jobs, Cities
from .forms import MassegeForm
from django.views.generic.edit import FormMixin
from django.urls import reverse


class JobListView(ListView):
    model = Jobs
    template_name = 'jobs/jobs_list.html'
    queryset = Jobs.objects.filter(status='p')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobcount"] = Jobs.objects.filter(status='p').count()
        return context


class JobCreate(LoginRequiredMixin, FormValidMixin, CreateView):
    model = Jobs
    template_name = 'jobs/add_job.html'
    success_url = reverse_lazy('index')
    fields = [
        "title",
        "company",
        "description",
        "address",
        "important",
        "price",
        "category",
        "city",
        "Type",
        "soldiering",
        "sex",
        'service',
        'employer_description', ]


class JobsDetailView(FormMixin, DetailView):
    model = Jobs
    template_name = 'jobs/jobDetail.html'
    form_class = MassegeForm

    def get_queryset(self):
        return Jobs.objects.filter(status='p')

    def get_success_url(self):
        return reverse('job-detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.revicer = self.object.author
        form.save()
        return super().form_valid(form)


class SearchjobsView(ListView):
    template_name = 'jobs/job_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = Cities.objects.all()
        return context

    def get_queryset(self):
        request = self.request
        type = request.GET.get('type')
        city = request.GET.get('city')
        title = request.GET.get('title')
        if type is not None:
            return Jobs.objects.filter(Type__icontains=type)
        if city is not None:
            return Jobs.objects.filter(city__title__icontains=city)
        if title is not None:
            return Jobs.objects.filter(title__icontains=title)