

from blog.models import Article, Category

from django.shortcuts import render
from django.http import HttpResponseRedirect


def featured(request):

    recent_articles = Article.objects.filter(published = True).order_by('-release_date')[:5]

    return render(
        request,
        "blog/reader/featured.html",
        {
            'Categories': Category.objects.all(),
            "articles": recent_articles,
        },
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
        {
            'Categories': Category.objects.all(),
            "article": article
        }
    )


def author_view(request):

    return render(
        request,
        "blog/author/article.html",
        {"articles": Article.objects.all()}
    )


def article_writer(request, article_id):

    pass