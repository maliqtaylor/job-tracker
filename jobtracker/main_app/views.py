from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Application
from .forms import InterviewForm
# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def application_index(request):
  applications = Application.objects.all()
  return render(request, 'applications/index.html', { 'applications': applications })

def app_detail(request, app_id):
  app = Application.objects.get(id=app_id)
  interview_form = InterviewForm()
  return render(request, 'applications/detail.html', { 'app': app, 'interview_form': interview_form })

def add_interview(request, app_id):
  form = InterviewForm(request.POST)
  if form.is_valid():
    new_interview = form.save(commit=False)
    new_interview.application_id = app_id
    new_interview.save()
  return redirect('detail', app_id=app_id)

class ApplicationCreate(CreateView):
  model = Application
  fields = ['company', 'location', 'title']

class ApplicationUpdate(UpdateView):
  model = Application
  fields = ['location', 'title']

class ApplicationDelete(DeleteView):
  model = Application
  success_url = '/applications/'