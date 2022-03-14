from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')
