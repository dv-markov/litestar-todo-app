from dataclasses import dataclass
from litestar import Litestar, get
from litestar.exceptions import HTTPException


@dataclass
class TodoItem:
    title: str
    done: bool


TODO_LIST: list[TodoItem] = [
    TodoItem(title="Start writing TODO list", done=True),
    TodoItem(title="???", done=False),
    TodoItem(title="Profit", done=False),
]


# Пример II.03.01 - базовое использование параметров запроса без проверки входных данных
@get(path="/string-query")
async def get_list2(done: str) -> list[TodoItem]:
    if done == "1":
        return [item for item in TODO_LIST if item.done]
    return [item for item in TODO_LIST if not item.done]


# Пример II.03.02 - проверка входных данных внутри функции
@get("string-query-check/")
async def get_list3(done: str) -> list[TodoItem]:
    if done == "1":
        return [item for item in TODO_LIST if item.done]
    if done == "0":
        return [item for item in TODO_LIST if not item.done]
    raise HTTPException(f"Invalid query parameter value: {done!r}", status_code=400)


# Пример II.03.02 - приведение типов и валидация за счет аннотации типов
@get("/")
async def get_list(done: bool) -> list[TodoItem]:
    return [item for item in TODO_LIST if item.done == done]


app = Litestar([get_list2, get_list3])