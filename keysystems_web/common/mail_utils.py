from django.core.mail import send_mail, EmailMessage


# Определяет начальную страницу пользователя
def send_pass_email(email: str, password: str) -> None:
    send_mail(
        subject='Пароль',
        message=f'Ваш пароль для входа в кабинет {password}',
        from_email='no-reply@gmail.com',
        recipient_list=[email],
        fail_silently=False
    )
