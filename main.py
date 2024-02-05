# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person(name={self.name}, age={self.age})"

#     def __repr__(self) -> str:
#         return f"Driver version 3.29.0"


# p = Person("John", 30)
# print(repr(p))
# print(p)  # Person(name=John, age=30)

#############################################
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __eq__(self, other: "Person") -> bool:
#         if isinstance(other, Person):
#             return self.name == other.name and self.age == other.age
#         return False


# p1 = Person("John", 30)
# p2 = Person("John", 30)
# p3 = Person("Jane", 25)

# print(p1 == p2)  # True
# print(p1 == p3)  # False

#############################################


# class Vector:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

#     def __add__(self, other: "Vector") -> "Vector":
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         raise TypeError(
#             "unsupported operand type(s) for +: 'Vector' and '{}'".format(
#                 type(other).__name__
#             )
#         )


# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3.x, v3.y)  # 4 6

#############################################


# class MyList:
#     def __init__(self, items: list):
#         self.items = items

#     def __len__(self) -> int:
#         return len(self.items)


# ml = MyList([1, 2, 3, 4, 5])
# print(len(ml))  # 5


#############################################

# class MyNumber:
#     def __init__(self, num: int):
#         self.num = num

#     def __bool__(self):
#         return bool(self.num)

#     def __len__(self) -> int:
#         return 1

# mn = MyNumber(5)
# print(bool(mn)) # True
# mn2 = MyNumber(0)
# print(bool(mn2)) # False
# print(len(mn)) # 1


#############################################


class MyDict:
    def __init__(self, data: dict):
        self.data = data

    def __getitem__(self, key: str):
        return self.data[key]


md = MyDict({"a": 1, "b": 2})
print(md["a"])  # 1
