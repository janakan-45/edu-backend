from django.urls import path
from . import views

urlpatterns = [
    path('api/universities/', views.university_list, name='university-list'),
]
