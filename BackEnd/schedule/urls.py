from django.urls import path
from . import views

urlpatterns = [
    path('',views.dosch,name='dosch'),
    path('new.html',views.donew,name='donew'),
    path('createschedule.html',views.docreateschedule,name='docreateschedule'),
    path('update.html',views.doupdate,name='doupdate'),
    path('delete',views.dodelete,name='dodelete'),
    path('change.html',views.dochange,name='dochange'),
    path('remove.html',views.doremove,name='doremove'),
    path('reschedule.html',views.doreschedule,name='doreschedule'),
    path('choosecategory.html',views.dochoosecategory,name='dochoosecategory'),
    path('searchid',views.dosearchid,name='dosearchid'),
    path('searchcity',views.dosearchcity,name='dosearchcity'),
    path('city.html',views.docity,name='docity'),
    path('id.html',views.doid,name='doid'),
]