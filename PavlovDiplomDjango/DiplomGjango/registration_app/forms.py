from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):

    #Форма регистрации нового пользователя на сайте.

    #Для создания формы используется crispy-forms, шаблон полей создается в __init__.


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
    repeat_password = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control my-3",
                "placeholder": "Повторите пароль",
                "id": "ReInputPassword",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        #При создании объекта класса - FormHelper создаст html шаблон форм

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "username",
            "password",
            "repeat_password",
            Submit(
                "submit",
                "Регистрация",
                css_class="btn my-3 btn-lg btn-primary btn-block",
            ),
        )

    def clean(self):
        #Автоматически проверит заполненную форму на наличие username в базе данных и проверит корректность пароля

        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["repeat_password"]

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        elif User.objects.filter(username=username):
            raise forms.ValidationError("Пользователь с таким именем существует")

    def save_new_user(self):
        #Внести данные нового пользователя в таблицу User. И аутентифицировать его

        new_user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"],
        )
        new_user.save()
