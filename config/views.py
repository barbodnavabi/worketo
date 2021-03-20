from django.shortcuts import render

from jobs.models import Jobs


def index(request):
    jobs = Jobs.objects.filter(status='p')
    context = {
        'jobs': jobs,

    }
    return render(request, 'config/index.html', context)
