from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from jobs.models import Jobs


class JobCreate(CreateView):
    model = Jobs
    template_name = 'jobs/add_job.html'
    success_url = reverse_lazy('index')
    fields = ["author",
              "title",
              "company",
              "description",
              "address",
              "important",
              "services",
              "price",
              "category",
              "city",
              "Type",
              "status",
              "soldiering", ]
