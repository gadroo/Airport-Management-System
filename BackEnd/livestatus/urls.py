from . import views
from django.urls import path

urlpatterns = [
    path('',views.doinit,name='doinit'),
    path('lpassogood',views.dolpassogood,name='dolpassogood'),
    path('lflight',views.dolflight,name='dolfight'),
    path('livef',views.dolivef,name='dolivef'),
    path('livepg',views.dolivepg,name='dolivepg'),
]