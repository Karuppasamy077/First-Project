from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls,name='Adminpanel'),

    path('', views.register_view, name='Register'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),


    path('home/', views.home, name='Home'),
    path('insert/', views.insert, name='Insert'),
    path('details/', views.details, name='Details'),


    path('update/', views.update, name='Update'),
    path('update2/<id>', views.update2, name='Update2'),

    path('delete/', views.delete, name='Delete'),
    path('delete2/<id>', views.delete2, name='Delete2'),

    path('contact/', views.contact, name='Contact'),
    path('about/', views.about, name='About'),

]
