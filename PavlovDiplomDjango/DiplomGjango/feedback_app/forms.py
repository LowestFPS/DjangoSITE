from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms


class FeedBackForm(forms.Form):


    name = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ваше имя",
                "id": "inputName",
            }
        ),
    )
    email = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ваша почта",
                "id": "inputEmail",
            }
        ),
    )
    subject = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Тема",
                "id": "inputSubject",
            }
        ),
    )
    message = forms.CharField(
        label="",
        max_length=255,
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Ваше сообщение",
                "id": "inputMessage",
            }
        ),
    )

    def __init__(self, *args, **kwargs):


        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="form-group col-md-6"),
                Column("email", css_class="form-group col-md-6"),
                css_class="form-row",
            ),
            "subject",
            "message",
            Submit("submit", "Отправить", css_class="btn btn-primary"),
        )
