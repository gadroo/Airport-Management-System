from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
    path('',views.dohome,name='dohome'),
    path('login/', views.dologin, name='dologin'),
    path('doauth',views.doauth,name='doauth'),
    path('logout/',views.dologout,name='dologout'),
]