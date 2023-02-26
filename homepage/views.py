from django.shortcuts import render, HttpResponse
from django.conf import settings


def home(request):

    return render(
        request,
        'index.html'
    )