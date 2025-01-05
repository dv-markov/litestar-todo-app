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
print(normalize_id("user-01"))


# Local type inference
def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output = []
    for num in numbers:
        if num < limit:
            output.append(num)
    return output


print(nums_below(range(100), 5.1))


# Types from libraries
# Mypy can also understand how to work with types from libraries that you use.
# For instance, mypy comes out of the box with an intimate knowledge of the Python standard library.
# For example, here is a function which uses the Path object from the pathlib standard library module:
from pathlib import Path


def load_template(template_path: Path, name: str) -> str:
    # Mypy knows that `template_path` has a `read_text` method that returns a str
    template = template_path.read_text() + 'USERNAME'
    # ...so it understands this line type checks
    return template.replace('USERNAME', name)


print(load_template(Path('/dev/null'), 'template.html'))

# If a third party library you use declares support for type checking, mypy will type check your use of that library
# based on the type hints it contains.
#
# However, if the third party library does not have type hints, mypy will complain about missing type information.
#
# prog.py:1: error: Library stubs not installed for "yaml"
# prog.py:1: note: Hint: "python3 -m pip install types-PyYAML"
# prog.py:2: error: Library stubs not installed for "requests"
# prog.py:2: note: Hint: "python3 -m pip install types-requests"
# ...
# In this case, you can provide mypy a different source of type information, by installing a stub package.
# A stub package is a package that contains type hints for another library, but no actual code.
#
# $ python3 -m pip install types-PyYAML types-requests
# Stubs packages for a distribution are often named types-<distribution>. Note that a distribution name may be
# different from the name of the package that you import. For example, types-PyYAML contains stubs for the yaml package.

# mypy cheat sheet
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#explicit-types-for-variables
