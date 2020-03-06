from django.shortcuts import render 
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%A, %b %d, %Y %I:%M:%S", localtime())
    }
    return render(request, 'index.html', context)
    