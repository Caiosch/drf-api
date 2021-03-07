from django.shortcuts import render
import requests


def homepage(request): 
    return render(request, 'homepage.html', context={
        "message": "It's running!",
    })

def aboutpage(request):
    return render(request, 'aboutpage.html', context={})
