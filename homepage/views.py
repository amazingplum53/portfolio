from django.shortcuts import render, HttpResponseRedirect #HttpResponse
from portfolio.send import send_email
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def home(request):

    return render(
        request,
        'index.html',
        {"contact_form": ContactForm()}
    )

"""
from django.core.mail import send_mail

if form.is_valid():
    subject = form.cleaned_data["subject"]
    message = form.cleaned_data["message"]
    sender = form.cleaned_data["sender"]
    cc_myself = form.cleaned_data["cc_myself"]

    recipients = ["info@example.com"]
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect("/thanks/")
"""

def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            html_content = render_to_string(
                "contact_email.html", 
                {
                    "sender": form.cleaned_data["sender"],
                    "message": form.cleaned_data["message"]
                }
            )

            message = send_email(
                ["matthewpaulh@hotmail.co.uk"],
                form.cleaned_data["subject"],
                "contact" + settings.BASE_EMAIL_SENDER,
                html_content,
                cc = form.cleaned_data["sender"] if form.cleaned_data["cc_myself"] else []
            )

            message.send()

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