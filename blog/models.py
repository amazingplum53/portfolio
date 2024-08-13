
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

    views = IntegerField(default = 0)

    published = BooleanField(default = False)

    category = ForeignKey(Category, on_delete = CASCADE, null = True)

    content = TextField()

    def get_content(self):

        images = Image.objects.filter(article = self)

        paragraphs = self.content.split("\n")

        content = [p for p in paragraphs]

        for index, image in enumerate(images):

            content.insert(image.position + index, image)

        return content
    

class Image(Model):

    article = ForeignKey(Article, on_delete = CASCADE)

    source = ImageField(upload_to = "static/blog/images/ArticleImages/%Y/%m/")

    caption = CharField(max_length = 200)

    position = IntegerField() # No of paragraphs

