from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from loguru import logger

from authorization_app.authorization_services.services import authenticate_user
from authorization_app.forms import AuthorizationForm


class AuthorizationView(View):
    """Представление страницы авторизации пользователей. Я знаю, что есть стандартное в django. Это для учебы."""

    @logger.catch
    def get(self, request):
        """При get запросе будет выведен стандартный шаблон страницы с формой авторизации."""

        return render(
            request,
            "authorization_app/authorization_page.html",
            context={"form": AuthorizationForm()},
        )

    @logger.catch
    def post(self, request):
        """После проверки корректности формы пользователь будет авторизован и перенаправлен на главную станицу."""

        form = AuthorizationForm(request.POST)
        error = ""
        if form.is_valid():
            user = authenticate_user(form)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = "Логин или пароль неверный"
        return render(
            request,
            "authorization_app/authorization_page.html",
            context={"form": form, "error": error},
        )
