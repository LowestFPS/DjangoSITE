from django.contrib.auth import authenticate


def authenticate_user(user):
    """Аутентификация пользователя."""

    return authenticate(**user.cleaned_data)
