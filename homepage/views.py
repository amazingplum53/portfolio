from django.shortcuts import render #HttpResponse

from .forms import ContactForm


def home(request):

    return render(
        request,
        'index.html',
        {"contact_form": ContactForm}
    )


def contact(request):

    return render(
        request,
        'contact.html',
        {"contact_form": ContactForm}
    )


def projects(request):

    return render(
        request,
        'projects.html',
        {"contact_form": ContactForm}
    )