from django.shortcuts import render

# Create your views here.
def app2_file(request):
    d={'mobile':6301686466}
    return render(request,'app2_file.html',d)