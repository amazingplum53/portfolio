from django.shortcuts import render


def featured(request):

    return render(
        request,
        "featured.html"
    )
