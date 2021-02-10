from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('applications/', views.application_index, name='index'),
  path('applications/<int:app_id>/', views.app_detail, name='detail'),
  path('applications/create/', views.ApplicationCreate.as_view(), name='applications_create'),
  path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name='applications_update'),
  path('items/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='applications_delete'),
  path('applications/<int:app_id>/add_interview/', views.add_interview, name='add_interview'),
  path('accounts/signup/', views.signup, name='signup'),
]