from django.http import HttpResponse
from django.shortcuts import render

# here are the functions that send you to the url you've specified

def home(request):
    return render(request, 'home.html')


def about(request):
    return HttpResponse('Eggs are great!')


def users(request):
    return render(request, 'users.html')