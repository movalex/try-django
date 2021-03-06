from django.http import HttpResponse

from articles.models import Article
from random import randint


def home_view(request):
    number = randint(2, 4)
    article_obj = Article.objects.get(id=number)
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = """
    <H1>{title}</H1>
    
    <p>{content} with id: {id}</p>
    """.format(**context)

    return HttpResponse(HTML_STRING)
