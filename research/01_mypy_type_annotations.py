from typing import Iterable

# mypy tutorial https://mypy.readthedocs.io/en/stable/getting_started.html

# здесь mypy укажет на несоответствие и python сгенерит ошибку
# number: int = input("What is your favourite number?")
# print("It is", number + 1)

# здесь - все ок
# number: int = int(input("What is your favourite number?"))
# print("It is", number + 1)


# Dynamic vs static typing
# A function without type annotations is considered to be dynamically typed by mypy:
# def greeting(name):
#     return 'Hello ' + name
#
#
# print(greeting("Winnie!"))

# Интерпретатор выдаст ошибку, но mypy ничего не напишет, потому что функция и аргументы типизированы динамически
# greeting(123)
# greeting(b"Alice")


# We can get mypy to detect these kinds of bugs by adding type annotations (also known as type hints).
# For example, you can tell mypy that greeting both accepts and returns a string like so:
def greeting(name: str) -> str:
    return 'Hello ' + name


# greeting(3)         # Argument 1 to "greeting" has incompatible type "int"; expected "str"
# greeting(b'Alice')  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting("World!")  # No error

# # Unsupported operand types for * ("str" and "str")
# def bad_greeting(name: str) -> str:
#     return 'Hello ' * name


# More complex types
def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
# greet_all(ages)    # Error due to incompatible types


# Вместо конкретного составного типа - списка, кортежа или множества - лучше указать Iterable,
# тогда функция примет на вход любую коллекцию
def greet_all_2(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)


names_tuple = tuple(names)
print(names)
print(names_tuple)

# Функция принимает на вход любой тип коллекции
greet_all_2(names)
greet_all_2(names_tuple)


# As another example, suppose you want to write a function that can accept either ints or strings, but no other types.
# You can express this using a union type. For example, int is a subtype of int | str:
def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    else:
        return user_id


print(normalize_id(55))
print(normalize_id(55))