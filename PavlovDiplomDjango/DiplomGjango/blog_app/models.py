from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class PostModel(models.Model):
    """Таблица хранящая данные отдельного поста из блога."""

    heading = models.CharField(max_length=255, verbose_name="Цена")
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(blank=True, null=True, verbose_name="Картинка")
    url = models.SlugField(verbose_name="Имя ссылки на ваш пост")
    description = models.TextField(verbose_name="Описание")
    content = RichTextUploadingField(verbose_name="Описание")
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, verbose_name="Автор")
    created_data = models.DateField(default=timezone.now, verbose_name="Дата создания")
    tag = TaggableManager(blank=True, verbose_name='Теги (латинскими буквами)')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class CommentModel(models.Model):
    """Таблица хранящая данные комментария под постом."""

    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "comments"
        ordering = ['-created_date']
        verbose_name = "Комментарии"

    def __str__(self):
        return self.text
