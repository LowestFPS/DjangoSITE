from django.core.mail import send_mail

from django_rest_blog.settings import EMAIL_HOST_USER


def send_mail_from_form(feedback_form: dict, for_email=EMAIL_HOST_USER) -> None:
    """Отправляет корректную форму feedback_form на почту установленную в параметр for_email."""

    send_mail(
        f'От {feedback_form["name"]} | {feedback_form["subject"]}',
        f'{feedback_form["message"]} \n\n\n Email для ответа: {feedback_form["email"]}',
        for_email,
        [for_email],
    )
