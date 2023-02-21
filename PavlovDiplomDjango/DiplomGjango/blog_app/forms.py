from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Column
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea

from blog_app.models import PostModel, CommentModel


class CreatePostForm(ModelForm):
    """
    Форма создания нового поста в блоге. Основана на модели PostModel.

    Для создания формы используется crispy-forms, шаблон полей создается в __init__.
    """

    class Meta:
        model = PostModel
        fields = [
            "heading",
            "title",
            "image",
            "description",
            "content",
            "tag",
        ]

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column("heading", css_class="form-group text-center"),
            Column("title", css_class="form-group text-center"),
            Column("image", css_class="form-group text-center"),
            Column("description", css_class="form-group text-center"),
            Column("content", css_class="form-group text-center"),
            Column("tag", css_class="form-group text-center"),
            Submit(
                "submit",
                "Опубликовать",
                css_class="btn my-3 btn-lg btn-primary btn-block",
            ),
        )

    def clean(self):
        """Валидация поля tag на наличие латинских символов и отсутствие любых других."""

        en_alphabet_lower = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
        invalid_symbols = (
            ":", ";", "%", "&", "?", "/", "<", ">", ".", "}", "{", "[", "]", "^", "*", "(", ")", "+", "=",
        )

        if not self.cleaned_data['tag']:
            raise ValidationError("Поле тег не должно быть пустым")

        list_all_tags = [tag for tag in self.cleaned_data['tag']]

        for word in list_all_tags:
            for letter in word:
                if letter.lower() not in en_alphabet_lower:
                    raise ValidationError("Буквы должны быть латинскими")
                elif letter in invalid_symbols:
                    raise ValidationError("В теге присутствуют лишние символы. Должны быть только буквы или тире")


class CommentForm(ModelForm):
    """
    Форма создания нового комментария. Основана на модели CommentModel.

    Для создания формы используется crispy-forms, шаблон полей создается в __init__.
    """

    class Meta:
        model = CommentModel
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'text',
            HTML('<input type="submit" value="Отправить" class="btn my-3 btn-primary btn-block">'),
        )
