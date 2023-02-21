from django.shortcuts import get_object_or_404
from taggit.models import Tag


def get_tag_or_404(slug: str):
   #Вернет тег полученный из поля slug, если он есть в таблице тегов или 404, если такого нет

    return get_object_or_404(Tag, slug=slug)
