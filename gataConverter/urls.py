

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.downloadFile, name='download'),
    path('sampleFile', views.sampleFile, name='sampleFile'),
    path('manual', views.manual, name='manual'),
]

