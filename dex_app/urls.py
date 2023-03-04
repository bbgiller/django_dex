from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('current_glucose/', views.current_glucose, name='current_glucose'),
    path('glucose_readings_list/', views.glucose_readings_list, name='glucose_readings_list'),
]
