

from blog.models import Article
from context_processor import category_context_processor

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext


def featured(request):

    recent_articles = Article.objects.filter(published = True).order_by('-release_date')[:5]

    return render(
        request,
        "blog/reader/featured.html",
        {"articles": recent_articles},
        context_instance = RequestContext(request, processors=[category_context_processor])
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
        "blog/reader/article.html",
        {"article": article},
        context_instance = RequestContext(request, processors=[category_context_processor])
    )


def author_view(request):

    return render(
        request,
        "blog/author/article.html",
        {"articles": Article.objects.all()},
        context_instance = RequestContext(request, processors=[category_context_processor])
    )


def article_writer(request, article_id):

    pass