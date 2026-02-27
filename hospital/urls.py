"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list,  name='appointment_list'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('edit-doctor/<int:id>/', views.edit_doctor, name='edit_doctor'),
    path('delete-doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('edit-patient/<int:id>/', views.edit_patient, name='edit_patient'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('edit-appointment/<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('delete-appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
]
