from django.shortcuts import render, HttpResponseRedirect #HttpResponse
from portfolio.send import send_email
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def home(request):

    return render(
        request,
        'homepage/index.html',
        {"contact_form": ContactForm()}
    )


def contact(request):

    form = ContactForm(request.POST)

    if request.method == "POST":

        if form.is_valid():

            html_content = render_to_string(
                "contact_email.html", 
                {
                    "sender": form.cleaned_data["sender"],
                    "message": form.cleaned_data["message"],
                }
            )

            send_email(
                ["matthewpaulh@hotmail.co.uk"],
                form.cleaned_data["subject"],
                "contact" + settings.BASE_EMAIL_SENDER,
                html_content,
                cc = [form.cleaned_data["sender"]] if form.cleaned_data["cc_myself"] else []
            )

        return render(request, "homepage/contact.html", {})
    
    else:

        return HttpResponseRedirect("/homepage/about/")


def projects(request):

    return render(
        request,
        'homepage/projects.html',
        {"contact_form": ContactForm()}
    )