import smtplib

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from loguru import logger

from .feedback_services.services import send_mail_from_form
from .forms import FeedBackForm


class FeedBackView(View):
    #Представление страницы отправки обратной связи.

    @logger.catch
    def get(self, request):
        #Отображает шаблона страницы с формой и заголовком.

        form = FeedBackForm()
        return render(
            request,
            "feedback_app/contacts_page.html",
            context={"form": form, "title": "Написать мне"},
        )

    @logger.catch
    def post(self, request):

        #При корректно введенной форме, и корректных настройках email в settings.py отправит сообщение на ваш email.


        form = FeedBackForm(request.POST)

        if form.is_valid():
            try:
                send_mail_from_form(feedback_form=form.cleaned_data)
            except smtplib.SMTPAuthenticationError:
                logger.exception(
                    "Произошла ошибка при отправке формы обратной связи. Проверьте корректность email и email_app_key "
                    "установленных в settings.py"
                )
            return HttpResponseRedirect("thanks")
        return render(
            request,
            "feedback_app/contacts_page.html",
            context={
                "form": form,
            },
        )


class ThanksView(View):
    #Представление для отображения страницы с благодарностью, после отправки обратной связи.

    @logger.catch
    def get(self, request):
        return render(
            request,
            "feedback_app/thanks_page.html",
            context={"title": "Спасибо"},
        )
