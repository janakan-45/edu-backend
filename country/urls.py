from django.urls import path
from . import views

urlpatterns = [
    path('api/countries/', views.country_list, name='country-list'),
]
