from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Application
from .forms import InterviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def application_index(request):
  applications = Application.objects.filter(user=request.user)
  return render(request, 'applications/index.html', { 'applications': applications })

@login_required
def app_detail(request, app_id):
  app = Application.objects.get(id=app_id)
  interview_form = InterviewForm()
  return render(request, 'applications/detail.html', { 'app': app, 'interview_form': interview_form })

@login_required
def add_interview(request, app_id):
  form = InterviewForm(request.POST)
  if form.is_valid():
    new_interview = form.save(commit=False)
    new_interview.application_id = app_id
    new_interview.save()
  return redirect('detail', app_id=app_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ApplicationCreate(LoginRequiredMixin, CreateView):
  model = Application
  fields = ['company', 'location', 'title']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class ApplicationUpdate(LoginRequiredMixin, UpdateView):
  model = Application
  fields = ['location', 'title']

class ApplicationDelete(LoginRequiredMixin, DeleteView):
  model = Application
  success_url = '/applications/'