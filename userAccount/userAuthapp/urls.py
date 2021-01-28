from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.loginUser, name= 'login' ),
    path('', views.index, name= 'Login-SignUp' ),
    path('register/', views.register, name= 'register' ),
    path('content/', views.content, name= 'content' ),
    path('logoutUser/', views.logoutUser, name= 'logoutUser' ),

    
]
