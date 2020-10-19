from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def project_detail(request, project_id):
    project = Job.objects.get(id=project_id)
    return render(request, 'jobs/project.html', {'project': project})