from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]