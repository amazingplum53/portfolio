
from django.shortcuts import render

from blog.models import Article

from django.http import HttpResponseRedirect

def featured(request):

    recent_articles = Article.objects.filter(published = True).order_by('-release_date')[:5]

    return render(
        request,
        "featured.html",
        {"articles": recent_articles}
    )


def article(request, article_id):

    article = Article.objects.get(id = article_id)

    if not article.published:

        return HttpResponseRedirect("/blog/featured/")

    return render(
        request,
        "featured.html",
        {"articles": article}
    )