from django.db.models import Q
from django.shortcuts import get_object_or_404

from blog_app.models import PostModel, CommentModel


def get_post_or_404(url: str):
    """Возвращает определенный пост из таблицы PostModel по url, или 404."""

    return get_object_or_404(PostModel, url=url)


def get_posts_where_tag(tag_name: str):
    """Возвращает QuerySet постов из таблицы PostModel. Где присутствует тег tag_name."""

    return PostModel.objects.filter(tag=tag_name)


def get_common_tags_from_posts_table():
    """
    Возвращает QuerySet со всеми часто используемыми тегами при помощи метода most_common.

    Поскольку постов немного в тестовой версии сайта, выводятся все посты у которых больше 2 упоминаний.
    """

    return PostModel.tag.most_common(2)


def get_five_last_posts_in_posts_table(open_post_url: str):
    """Возвращает QuerySet пяти последних постов из таблицы PostModel без открытого поста с open_post_url."""

    return PostModel.objects.exclude(url=open_post_url)[::-1][:5]


def get_all_posts_from_blog():
    """Возвращает QuerySet всех постов в таблице PostModel. В обратном порядке."""

    return PostModel.objects.all()[::-1]


def get_last_post_id_from_post_table() -> str:
    """Возвращает строку с id последнего объекта в таблице PostModel."""

    last_post_id, = PostModel.objects.values('id').order_by('-id')[:1]
    return last_post_id['id']


def find_query_in_posts_table(query: str):
    """
    Возвращает QuerySet из тех постов, в который найден запрос query. Выводит начиная с самого нового.

    Поиск происходит в заголовках и основном контенте поста.
    """

    return PostModel.objects.filter(
        Q(heading__icontains=query) | Q(content__icontains=query)
    )[::-1]


def create_new_post_for_post_table(heading: str, title: str, description: str, content: str, author: str,
                                   tag: str, image: str) -> None:
    """
    Добавляет новый пост в таблицу PostModel.

    Поле slug заполняется следующим номером id после последнего поста.
    Чтобы добавить теги полученные из формы TaggableManager, используем апдейт созданного поля и разделяем теги запятой.
    """

    last_post_id = get_last_post_id_from_post_table()

    PostModel.objects.create(
        heading=heading,
        title=title,
        image=image,
        url=f'post-{int(last_post_id) + 1}',
        description=description,
        content=content,
        author=author,
    )

    new_post = PostModel.objects.get(url=f'post-{int(last_post_id) + 1}')
    for one_tag in tag.replace(" ", "").split(','):
        new_post.tag.add(one_tag)


def create_new_comment_for_comments_table(post: str, username: str, text: str):
    """
    Добавляет новый комментарий в таблицу CommentModel.

    Комментарий c информацией text для поста post от пользователя username.
    """

    return CommentModel.objects.create(post=post, username=username, text=text)
