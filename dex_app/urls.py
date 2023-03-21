from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('current_glucose/', views.current_glucose, name='current_glucose'),
    path('glucose_readings_list/', views.glucose_readings_list, name='glucose_readings_list'),
    path('create_user/', views.create_user, name='create_user'),
    path('get_user/<int:id>/', views.get_user, name='get_user'),
    path('create_insulin/', views.create_insulin, name='create_insulin'),
]
