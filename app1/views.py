from django.shortcuts import render

# Create your views here.
def app1_file(request):
    d={'name':'ANIL'}
    return render(request,'app1_file.html',d)