# Задача 1. Права доступа
# Что нужно сделать
# Перед вами стоит задача создать и поддерживать специализированный форум. Вы только приступили и сейчас работаете
# над действиями, которые могут совершать посетители форума. Для разных пользователей прописаны разные возможности.
# Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к вызываемой функции,
# и если нет, то выдаёт исключение PermissionError.
# Пример кода:
# user_permissions = ['admin']
#
# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')
#
# @check_permission('user_1')
# def add_comment():
#     print('Добавляем комментарий')
#
# delete_site()
# add_comment()
# Результат:
# Удаляем сайт
# PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment

import functools
from typing import Callable, Any


class PermissionError(Exception):
    def __init__(self, message: str = 'у пользователя недостаточно прав, чтобы выполнить функцию') -> None:
        self.message = message
        super().__init__(message)

    def print_error(self) -> None:
        print(self.message)


def check_permission(allowed_users: list) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(current_user: str, *args, **kwargs) -> Any:
            if current_user in allowed_users:
                print('ok')
                return func(current_user, *args, **kwargs)
            else:
                return PermissionError().print_error()
        return wrapper
    return decorator


@check_permission(['admin'])
def delete_site(current_user: str) -> None:
    print('Удаляем сайт')


@check_permission(['admin', 'user'])
def add_comment(current_user: str) -> None:
    print('Добавляем комментарий')


user_1 = 'admin'
user_2 = 'user'
delete_site(current_user=user_2)
add_comment(current_user=user_2)
