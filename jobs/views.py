from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,DetailView

from jobs.mixins import FormValidMixin,RevicerMixin
from jobs.models import Jobs,Cities
from .forms import MassegeForm

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
        "soldiering",
        "sex",
         'service',
         'employer_description',]


class JobsDetailView(RevicerMixin,DetailView):
    model = Jobs
    template_name = 'jobs/job_detail.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["massegeform"] = MassegeForm(self.request.POST or None)
        return context
    

    def get_queryset(self):
        return Jobs.objects.filter(status='p')

    
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
        # type = request.GET.get('Type')
        # if type is not None:
        #     return Jobs.objects.filter(Type__icontains=type)
