from django.shortcuts import render, HttpResponseRedirect #HttpResponse
from django.core.mail import EmailMessage

from .forms import ContactForm


def home(request):

    return render(
        request,
        'index.html',
        {"contact_form": ContactForm()}
    )


def contact(request):

    if request.method == "POST":

        try:

            message = EmailMessage(
                'Subject here',
                'Here is the message.',
                'support@matthewhill.click',
                ['matthewpaulh@hotmail'],
            )

            message.send()

        except Exception as e:
            
            raise e

    else:

        return HttpResponseRedirect("/homepage/about/")

    return render(
        request,
        'contact.html',
    )


def projects(request):

    return render(
        request,
        'projects.html',
        {"contact_form": ContactForm()}
    )