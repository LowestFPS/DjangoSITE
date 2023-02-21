from django.shortcuts import render
from django.views import View
from loguru import logger

from blog_app.blog_services.models_services import (
    find_query_in_posts_table,
    get_posts_where_tag,
    get_common_tags_from_posts_table,
)
from blog_app.blog_services.view_services import get_posts_for_page_from_result_of_find
from search_app.forms import SearchForm
from search_app.search_services.services import get_tag_or_404


class SearchResultsView(View):
    """Представление страницы поиска на сайте."""

    @logger.catch
    def get(self, request):
        """
        Отображает шаблон страницы поиска постов с формой поиска.

        При получении запроса из формы поиска выводит 10 найденных постов исходя из того какая страница выбрана.
        """

        result = ""
        if self.request.GET.get("query"):
            result = find_query_in_posts_table(query=self.request.GET.get("query"))
        return render(
            request,
            "search_app/search_page.html",
            context={
                "form": SearchForm(),
                "query": self.request.GET.get("query"),
                "result": get_posts_for_page_from_result_of_find(
                    result_of_find=result,
                    page_number=request.GET.get("page"),
                    quantity_posts_for_page=10,
                ),
                "count": len(result),
            },
        )


class TagView(View):
    #Представления страницы определенных тегов

    @logger.catch
    def get(self, request, slug):
        tag = get_tag_or_404(slug=slug)
        posts = get_posts_where_tag(tag_name=tag)
        common_tags = get_common_tags_from_posts_table()
        return render(
            request,
            "search_app/tag_page.html",
            context={
                "title": f"{tag}",
                "posts": posts,
                "common_tags": common_tags,
            },
        )
