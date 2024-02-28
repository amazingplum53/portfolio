
from django.db.models import (
    Model, TextField, CharField, 
    DateField, IntegerField, BooleanField, 
    ForeignKey, ImageField, CASCADE,
)


class Category(Model):

    name = CharField(max_length = 200)


class Article(Model):

    title = CharField(max_length = 200)

    release_date = DateField()

    views = IntegerField()

    published = BooleanField(default = False)

    category = ForeignKey(Category, on_delete = CASCADE, null = True)


    def get_content(self):

        content_types = [
            {"model": Paragraph, "objects": None},
            {"model": Image, "objects": None},
        ]

        content_length = 0

        for content_type in content_types:

            content_type["objects"] = content_type["model"].objects.filter(article = self).order_by("order")

            content_length += len(content_type["objects"])

        contents = [None] * content_length

        for content_type in content_types:

            for content in content_type["objects"]:

                contents[content.order] = content        

        return contents
    
    def first_paragraph(self):

        all_paragraphs = Paragraph.objects.filter(article = self)

        return all_paragraphs.order_by("order").first()
    

class Paragraph(Model):

    article = ForeignKey(Article, on_delete = CASCADE)

    text = TextField()

    order = IntegerField()

    def content_type(self):
        return "paragraph"
    

class Image(Model):

    article = ForeignKey(Article, on_delete = CASCADE)

    source = ImageField(upload_to = "static/blog/images/ArticleImages/%Y/%m/")

    caption = CharField(max_length = 200)

    order = IntegerField()

    def content_type(self):
        return "image"