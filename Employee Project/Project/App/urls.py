from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls,name='Adminpanel'),
    path('', views.home, name='Home'),
    path('details/', views.details, name='Details'),
    path('insert/', views.insert, name='Insert'),

    path('update/', views.update, name='Update'),
    path('update2/<id>', views.update2, name='Update2'),

    path('delete/', views.delete, name='Delete'),
    path('delete2/<id>', views.delete2, name='Delete2'),

    path('contact/', views.contact, name='Contact'),
    path('about/', views.about, name='About'),

]
