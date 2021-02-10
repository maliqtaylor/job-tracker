from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Applications
# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def application_index(request):
  applications = Applications.objects.all()
  return render(request, 'applications/index.html', { 'applications': applications })

def app_detail(request, app_id):
  app = Applications.objects.get(id=app_id)
  return render(request, 'applications/detail.html', { 'app': app })

class ApplicationCreate(CreateView):
  model = Applications
  fields = ['company', 'location', 'title']
  success_url = '/'

class ApplicationUpdate(UpdateView):
  model = Applications
  fields = ['location', 'title']
  success_url = '/'

class ApplicationDelete(DeleteView):
  model = Applications
  success_url = '/'

