from django.urls import path
from app2.views import *
app_name='two'

urlpatterns=[
    path('app2_file/',app2_file,name='app2_file'),
]