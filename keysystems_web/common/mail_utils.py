from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from datetime import datetime


# Определяет начальную страницу пользователя
def send_pass_email(email: str, password: str) -> None:
    send_mail(
        subject='Пароль',
        message=f'Ваш пароль для входа в кабинет {password}',
        from_email='no-reply@gmail.com',
        recipient_list=[email],
        fail_silently=False
    )


def send_password_email(user_email: str, password: str, login_url: str):
    subject = 'Ваш пароль для входа'
    message = render_to_string('email_password.html', {
        'password': password,
        'login_url': login_url,
        'year': datetime.now().year
    })
    email = EmailMessage(subject, message, to=[user_email])
    email.content_subtype = 'html'  # Отправляем как HTML
    email.send()