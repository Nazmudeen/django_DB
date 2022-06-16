from django.urls import path
from.import views

urlpatterns=[
    path('',views.index),
    path('add',views.addemployee),
    path('display',views.display),
    path('delete',views.delete,name='delete'),
    path('update',views.updates)
    
]