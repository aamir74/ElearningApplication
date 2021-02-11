from django.urls import path
from . import views

urlpatterns = [
    path('',views.home1,name='home1'),
    path('uvideo',views.uvideo,name='uvideo'),
    path('home1',views.home1,name='home1'),
    path('login',views.login,name='login'),
    path("logout",views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('class6',views.class6,name='class6'),
    path('maths',views.maths,name='maths'),
    path('search',views.search,name='search')
    
    ]
