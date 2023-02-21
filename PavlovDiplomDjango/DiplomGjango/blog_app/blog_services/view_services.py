from django.core.paginator import Paginator

from .models_services import get_all_posts_from_blog


def get_posts_for_page(page_number: str, quantity_posts_for_page: int):
    """
    Возвращает QuerySet определенного количества quantity_posts_for_page постов из таблицы PostModel.

    Возвращает в зависимости от номера выбранной страницы page_number.
    """

    all_posts = get_all_posts_from_blog()
    paginator = Paginator(all_posts, quantity_posts_for_page)
    posts_for_page = paginator.get_page(page_number)
    return posts_for_page


def get_posts_for_page_from_result_of_find(
        result_of_find: str, page_number: str, quantity_posts_for_page: int
):
    """
    Возвращает QuerySet определенного количества quantity_posts_for_page постов из result_of_find.

    В result_of_find передается QuerySet с постами из таблицы PostModel, которые совпали с поисковым запросом.
    Возвращает в зависимости от номера выбранной страницы page_number.
    """

    paginator = Paginator(result_of_find, quantity_posts_for_page)
    posts_for_page = paginator.get_page(page_number)
    return posts_for_page
