from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from jobs.mixins import FormValidMixin
from jobs.models import Jobs


class JobListView(ListView):
    model = Jobs
    template_name = 'jobs/job_list.html'
    queryset = Jobs.objects.filter(status='p')



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
        "soldiering", ]
