from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from loguru import logger

from .blog_services.models_services import (
    get_post_or_404,
    get_five_last_posts_in_posts_table,
    create_new_comment_for_comments_table, create_new_post_for_post_table,
)
from .blog_services.view_services import get_posts_for_page
from .forms import CreatePostForm, CommentForm


class BlogPageView(View):
    """Отображает страницу со всеми постами, поделенными на под-страницы пагинацией."""

    @logger.catch
    def get(self, request):
        return render(
            request,
            "blog_app/blog_page.html",
            context={
                "posts_for_page": get_posts_for_page(
                    page_number=request.GET.get("page"),
                    quantity_posts_for_page=6,
                )
            },
        )


class PostPageView(View):
    """Отображает страницу с полной информацией конкретного поста."""

    @logger.catch
    def get(self, request, url):
        """
        Отображает шаблон конкретного поста, если полученный url(slug) присутствует в таблице постов PostModel.

        В шаблоне отображается форма для добавления комментария.
        А так-же выводится пять последних опубликованных постов.
        """

        return render(
            request,
            "blog_app/post_page.html",
            context={
                'form': CommentForm(),
                "post": get_post_or_404(url=url),
                "last_posts": get_five_last_posts_in_posts_table(open_post_url=url),
            },
        )

    @logger.catch
    def post(self, request, url):
        """
        При получении данных заполненной формы, добавляет новый комментарий в таблицу CommentModel.

        После добавления комментария, перенаправляем пользователя на ту страницу с которой он был отправлен.
        Отправить комментарий может только зарегистрированный пользователь, проверка происходит в шаблоне.
        """

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            create_new_comment_for_comments_table(
                post=get_post_or_404(url=url),
                username=self.request.user,
                text=request.POST['text'],
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(
            request,
            'myblog/post_detail.html',
            context={
                'form': comment_form
            }
        )


class CreatePostPageView(View):
    """Отображает страницу с формой создания новой статьи для блога."""

    @logger.catch
    def get(self, request):
        """Выводит шаблон с формой создания статьи на странице."""

        return render(
            request,
            "blog_app/create_post_page.html",
            context={
                "form": CreatePostForm(),
            },
        )

    @logger.catch
    def post(self, request):
        """Получает данные введенной формы, создает новую статью в базе данных и перенаправляет на страницу блога."""

        form = CreatePostForm(request.POST)
        error = ""

        if form.is_valid():
            create_new_post_for_post_table(
                heading=request.POST['heading'],
                title=request.POST['title'],
                image=request.FILES.get('image', None),
                description=request.POST['description'],
                content=request.POST['content'],
                author=self.request.user,
                tag=request.POST['tag'],
            )
            return HttpResponseRedirect(reverse("blog"))
        else:
            error = "Форма заполнена некорректно, повторите попытку."
        return render(
            request,
            "blog_app/create_post_page.html",
            context={
                "error": error,
                "form": CreatePostForm(),
            },
        )
