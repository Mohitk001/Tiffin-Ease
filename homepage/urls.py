from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  
    path("", views.loggedIn, name="loggedin"),
    path('login/', views.index, name="login"),
    path('logout/', views.logoutUser, name="logout" ),
    path('register/', views.registerUser, name="register" ),
    # path('feedback/', views.feedback, name="feedback" )
    
]
