
from django.db.models import (
    Model, 
    TextField, 
    CharField, 
    DateField,
    IntegerField,
    BooleanField,
    ForeignKey,
    ImageField,
    CASCADE
)

class Article(Model):

    title = CharField(max_length = 200)

    content = TextField()

    release_date = DateField()

    views = IntegerField()

    published = BooleanField(default = False)


    def first_paragraph(self):

        return self.content.split("\n")[0]
    
    def paragraphs(self):

        return self.content.split("\n")
    

class Image(Model):

    article = ForeignKey(Article, on_delete = CASCADE)

    source = ImageField(upload_to = "ArticleImages/%Y/%m/")

    caption = CharField()
