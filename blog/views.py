
from django.shortcuts import render

from blog.models import Article

from django.http import HttpResponseRedirect


def featured(request):

    recent_articles = Article.objects.filter(published = True).order_by('-release_date')[:5]

    return render(
        request,
        "reader/featured.html",
        {"articles": recent_articles}
    )


def article(request, article_id):

    try:
        article = Article.objects.get(id = article_id)

    except:
        return HttpResponseRedirect("/blog/featured/")

    if not article.published:

        return HttpResponseRedirect("/blog/featured/")

    return render(
        request,
        "reader/article.html",
        {"articles": article}
    )


def author_view(request):

    return render(
        request,
        "author/article.html",
        {"articles": Article.objects.all()}
    )


def article_writer(request, article_id):

    pass