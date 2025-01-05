from dataclasses import dataclass, field

# Example of assignment of mutable type as default value
# Results incorrect behavior
# From:
# https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio
# https://peps.python.org/pep-0557/#mutable-default-values
class C:
    x = []
    def add(self, element):
        self.x.append(element)

o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
assert o1.x == [1, 2]
assert o1.x is o2.x
print(f'{o1.x=}\n{o2.x=}')


# Note that the two instances of class C share the same class variable x, as expected.
# Using Data Classes, if this code was valid:
#
# @dataclass
# class D:
#     x: List = []
#     def add(self, element):
#         self.x += element
# it would generate code similar to:
#
# class D:
#     x = []
#     def __init__(self, x=x):
#         self.x = x
#     def add(self, element):
#         self.x += element
#
# assert D().x is D().x


# This has the same issue as the original example using class C. That is, two instances of class D that do not specify a value for x when creating a class instance will share the same copy of x. Because Data Classes just use normal Python class creation they also share this problem. There is no general way for Data Classes to detect this condition. Instead, Data Classes will raise a TypeError if it detects a default parameter of type list, dict, or set. This is a partial solution, but it does protect against many common errors. See Automatically support mutable default values in the Rejected Ideas section for more details.
# Using default factory functions is a way to create new instances of mutable types as default values for fields:
@dataclass
class D:
    x: list = field(default_factory=list)
    def add(self, element):
        self.x.append(element)

assert D().x is not D().x
d1 = D()
d2 = D()
d1.add(1)
d2.add(2)
print(f'{d1.x=}\n{d2.x=}')
