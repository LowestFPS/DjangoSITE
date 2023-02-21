from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django import forms


class AuthorizationForm(forms.Form):
    """Форма авторизации пользователя на сайте."""

    username = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control my-3",
                "placeholder": "Введите имя пользователя",
                "id": "inputUsername",
            }
        ),
    )
    password = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control my-3",
                "placeholder": "Введите пароль",
                "id": "inputPassword",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "{% if error %} <p class='alert alert-danger'>{{ error }}</p> {% endif %}"
            ),
            "username",
            "password",
            Submit(
                "submit", "Войти", css_class="btn my-3 btn-lg btn-success btn-block"
            ),
        )
