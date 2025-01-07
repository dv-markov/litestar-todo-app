from dataclasses import dataclass
from litestar import Litestar, get
from litestar.exceptions import HTTPException


# Solution Using Python Data Classes
@dataclass
class TodoItem:
    title: str
    done: bool


TODO_LIST: list[TodoItem] = [
    TodoItem(title="Start writing TODO list", done=True),
    TodoItem(title="???", done=False),
    TodoItem(title="Profit", done=False),
]


# @get("/")
# async def get_list(done: str) -> list[TodoItem]:
#     if done == "1":
#         return [item for item in TODO_LIST if item.done]
#     if done == "0":
#         return [item for item in TODO_LIST if not item.done]
#     raise HTTPException(f"Invalid query parameter value: {done!r}", status_code=400)

@get("/")
async def get_list(done: bool) -> list[TodoItem]:
    return [item for item in TODO_LIST if item.done == done]


# Пример II.03 - базовое использование параметров запроса
# Составные адреса должны идти после прямых, потому что если функция имеет то же имя, она будет переопределена
@get(path="/string-query")
async def get_list2(done: str) -> list[TodoItem]:
    if done == "1":
        return [item for item in TODO_LIST if item.done]
    return [item for item in TODO_LIST if not item.done]


app = Litestar([get_list, get_list2])
