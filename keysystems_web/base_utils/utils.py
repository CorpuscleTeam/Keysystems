from random import choice


def pass_gen(len_: int = 8) -> str:
    return ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len_)])


# Получить ip
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Получить юзерагент
def get_user_agent(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    return user_agent
