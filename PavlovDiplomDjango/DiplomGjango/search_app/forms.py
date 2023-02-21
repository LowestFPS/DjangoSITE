from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class SearchForm(forms.Form):

    #Форма поиска определенного поста по введенному запросу на сайте.

    #Для создания формы используется crispy-forms, шаблон полей создается в __init__.


    query = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Поиск",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон формы."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.layout = Layout(
            "query",
            Submit("submit", "Поиск", css_class="btn btn-primary mt-3"),
        )
