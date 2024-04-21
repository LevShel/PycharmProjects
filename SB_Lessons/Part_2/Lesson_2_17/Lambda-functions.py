from typing import List

""" Код с помощью доп.функции """

# def string_to_int(elem: str) -> int:
#     return int(elem[4:])
#
#
# users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22', 'user100']
#
# sorted_users = sorted(users, key=string_to_int)
# print(sorted_users)


""" Код с помощью lambda-функции """

users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22', 'user100']

sorted_users = sorted(users, key=lambda elem: int(elem[4:]))
print(sorted_users)
