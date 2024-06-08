from . import views
from django.urls import path
urlpatterns = [
    path('',views.doinit,name='doinit'),
    path('flboarding',views.doflboarding,name='doflboarding'),
    path('flupdate',views.doflupdate,name='doflupdate'),
    path('boarding',views.doboarding,name='doboarding'),
    path('flightupdate',views.doflightupdate,name='doflightupdate'),
    path('reset',views.doreset,name='doreset'),
]