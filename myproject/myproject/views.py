#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html' ,{'home':homepage} )

def about(request):
    return render(request, 'about.html',{'about':about})

