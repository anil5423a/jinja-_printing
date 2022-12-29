from django.urls import path
from app1.views import *
app_name='one'

urlpatterns=[
    path('app1_file/',app1_file,name='app1_file'),
]