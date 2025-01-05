# здесь mypy укажет на несоответствие и python сгенерит ошибку
# number: int = input("What is your favourite number?")
# print("It is", number + 1)

# здесь - все ок
# number: int = int(input("What is your favourite number?"))
# print("It is", number + 1)


# Dynamic vs static typing
# A function without type annotations is considered to be dynamically typed by mypy:
def greeting(name):
    return 'Hello ' + name

print(greeting("Winnie!"))

# Интерпретатор выдаст ошибку, но mypy ничего не напишет, потому что функция и аргументы типизированы динамически
# greeting(123)
# greeting(b"Alice")

# We can get mypy to detect these kinds of bugs by adding type annotations (also known as type hints). For example, you can tell mypy that greeting both accepts and returns a string like so:

