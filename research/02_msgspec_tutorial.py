import msgspec
from dataclasses import field


class User(msgspec.Struct):
    """A new type describing a User"""
    name: str
    groups: set[str] = field(default_factory=set)
    email: str | None = None


alice = User("alice", groups={"admin", "engineering"})

print(alice)
alice.email = "alice@email.org"
print(alice)

# Encode messages as JSON, or one of the many other supported protocols
msg_encoded = msgspec.json.encode(alice)
print(f'{msg_encoded=}')

# Decode messages back into Python objects, with optional schema validation
msg_decoded = msgspec.json.decode(msg_encoded, type=User)
print(f'{msg_decoded=}')

# Проверка входных данных, данное сообщение проверку не пройдет из-за несоответствия типа данных:
# msgspec.json.decode(b'{"name":"bob","groups":[123]}', type=User)

# здесь все ок
msg_decoded_bob = msgspec.json.decode(b'{"name":"bob","groups":["123"]}', type=User)
print(f'{msg_decoded_bob=}')

# если не передать один из обязательных параметров типа field, то ошибка не сгенерится, но поле получит некорректное значение
msg_decoded_bob_2 = msgspec.json.decode(b'{"name":"bob"}', type=User)
print(f'{msg_decoded_bob_2=}')

# если не передать обязательный параметр типа поле, то получим ошибку msgspec.ValidationError: Object missing required field
# msg_decoded_bob_3 = msgspec.json.decode(b'{"groups":["123"]}', type=User)
# print(f'{msg_decoded_bob_3=}')
