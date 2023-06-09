from django.shortcuts import render, HttpResponseRedirect #HttpResponse
from portfolio.send import send_email
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def home(request):

    email_sent = False

    if request.method == "POST":

        email_sent = contact(request)



    return render(
        request,
        'index.html',
        {
            "contact_form": ContactForm(),
            "email_sent": email_sent
        }
    )


def contact(request):

    form = ContactForm(request.POST)

    if form.is_valid():

        html_content = render_to_string(
            "contact_email.html", 
            {
                "sender": form.cleaned_data["sender"],
                "message": form.cleaned_data["message"],
                "url": request.get_full_path()
            }
        )

        valid_response = send_email(
            ["matthewpaulh@hotmail.co.uk"],
            form.cleaned_data["subject"],
            "contact" + settings.BASE_EMAIL_SENDER,
            html_content,
            cc = form.cleaned_data["sender"] if form.cleaned_data["cc_myself"] else []
        )

        return valid_response


def projects(request):

    return render(
        request,
        'projects.html',
        {"contact_form": ContactForm()}
    )