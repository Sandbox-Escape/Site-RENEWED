from django.urls import path
from . import views

app_name = 'Main'

urlpatterns = [
    path('', views.index, name='index'),
    path('latest/', views.latest, name='latest'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
