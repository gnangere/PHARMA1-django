from django.urls import path
from . import  views


urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
     path('activate/uidb64/<token>/', views.activate, name='activate'),
 



]
