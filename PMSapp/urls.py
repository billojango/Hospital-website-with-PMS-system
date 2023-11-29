
from django.contrib import admin
from django.urls import path
from PMSapp import views
from .views import register
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('contacts/', views.contacts, name='contacts'),
    path('appointments/', views.appointments, name='appointments'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),
    path('upload/', views.upload_image, name='upload'),
    path('image/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)