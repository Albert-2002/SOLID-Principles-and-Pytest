# Complete Guide to Object-Oriented Programming in Python

## 1. Classes and Objects

### Basic Class Definition

```python
class Dog:
    pass

# Creating an object (instance)
my_dog = Dog()
print(type(my_dog))  # <class '__main__.Dog'>
```

### Class with Attributes and Methods

```python
class Dog:
    def bark(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.bark())  # Woof!
```

## 2. The `__init__` Constructor

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

my_dog = Dog("Buddy", 3)
print(my_dog.describe())  # Buddy is 3 years old
```

## 3. Instance Variables vs Class Variables

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    count = 0

    def __init__(self, name):
        # Instance variable (unique to each instance)
        self.name = name
        Dog.count += 1

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
print(Dog.count)     # 2
print(dog1.name)     # Buddy
print(dog2.name)     # Max
```

## 4. Instance Methods, Class Methods, and Static Methods

```python
class MyClass:
    class_var = "I'm a class variable"

    def __init__(self, value):
        self.instance_var = value

    # Instance method (has access to self)
    def instance_method(self):
        return f"Instance method called. Value: {self.instance_var}"

    # Class method (has access to cls, not self)
    @classmethod
    def class_method(cls):
        return f"Class method called. Class var: {cls.class_var}"

    # Static method (no access to self or cls)
    @staticmethod
    def static_method(x, y):
        return x + y

obj = MyClass(10)
print(obj.instance_method())      # Instance method called. Value: 10
print(MyClass.class_method())     # Class method called. Class var: I'm a class variable
print(MyClass.static_method(5, 3))  # 8
```

## 5. Encapsulation and Access Modifiers

```python
class BankAccount:
    def __init__(self, balance):
        self.public_var = "I'm public"
        self._protected_var = "I'm protected (convention)"
        self.__private_var = "I'm private"
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def __private_method(self):
        return "This is private"

    def call_private(self):
        return self.__private_method()

account = BankAccount(1000)
print(account.public_var)           # I'm public
print(account._protected_var)       # I'm protected (convention) - accessible but discouraged
# print(account.__private_var)      # AttributeError
print(account.get_balance())        # 1000
account.deposit(500)
print(account.get_balance())        # 1500

# Name mangling allows access (not recommended)
print(account._BankAccount__private_var)  # I'm private
```

## 6. Property Decorators (Getters, Setters, Deleters)

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        """Deleter for celsius"""
        print("Deleting temperature")
        del self._celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # 25 (calls getter)
print(temp.fahrenheit)   # 77.0
temp.celsius = 30        # calls setter
print(temp.celsius)      # 30
del temp.celsius         # Deleting temperature
```

## 7. Inheritance (Single Inheritance)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
```

## 8. The `super()` Function

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def description(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def description(self):
        base_desc = super().description()
        return f"{base_desc} of breed {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.description())  # Buddy is a Dog of breed Golden Retriever
```

## 9. Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())    # I can fly!
print(duck.swim())   # I can swim!
print(duck.quack())  # Quack!
```

## 10. Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # B (follows MRO: D -> B -> C -> A)
print(D.mro())     # Shows the method resolution order
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

## 11. Polymorphism

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 10), Circle(7), Rectangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
# Area: 50
# Area: 153.93791
# Area: 12
```

## 12. Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def breathe(self):
        return "Breathing..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Running on four legs"

# animal = Animal()  # TypeError: Can't instantiate abstract class
dog = Dog()
print(dog.speak())    # Woof!
print(dog.move())     # Running on four legs
print(dog.breathe())  # Breathing...
```

## 13. Magic Methods (Dunder Methods)

### `__str__` and `__repr__`

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # User-friendly string representation
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        # Developer-friendly representation
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "George Orwell")
print(str(book))   # '1984' by George Orwell
print(repr(book))  # Book('1984', 'George Orwell')
print(book)        # '1984' by George Orwell (uses __str__)
```

### Arithmetic Magic Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
print(v3)  # Vector(3, 7)
v4 = v1 * 3
print(v4)  # Vector(6, 9)
```

### Comparison Magic Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print(p1 < p2)   # True
print(p1 == p2)  # False
print(p1 > p2)   # False
```

### Container Magic Methods

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items

    def add(self, item):
        self.items.append(item)

cart = ShoppingCart()
cart.add("apple")
cart.add("banana")
cart.add("orange")

print(len(cart))           # 3
print(cart[1])             # banana
cart[1] = "grape"
print(cart[1])             # grape
print("apple" in cart)     # True
del cart[0]
print(len(cart))           # 2
```

### `__call__` Method

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

multiply_by_3 = Multiplier(3)
print(multiply_by_3(10))  # 30
print(multiply_by_3(5))   # 15
```

### Context Manager Methods

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

# Using the context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# File is automatically closed after the block
```

### Iterator Protocol

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(5):
    print(num, end=' ')  # 5 4 3 2 1
print()
```

## 14. Class Composition

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine starting..."

class Wheels:
    def __init__(self, count):
        self.count = count

    def roll(self):
        return f"{self.count} wheels rolling"

class Car:
    def __init__(self, horsepower, wheel_count):
        self.engine = Engine(horsepower)
        self.wheels = Wheels(wheel_count)

    def drive(self):
        return f"{self.engine.start()} {self.wheels.roll()}"

car = Car(200, 4)
print(car.drive())  # Engine starting... 4 wheels rolling
```

## 15. Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"
    hobbies: list = field(default_factory=list)

    def greet(self):
        return f"Hi, I'm {self.name}"

p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "bob@example.com", ["reading", "gaming"])
print(p1)  # Person(name='Alice', age=30, email='unknown@example.com', hobbies=[])
print(p2.greet())  # Hi, I'm Bob
```

## 16. Slots (Memory Optimization)

```python
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = WithoutSlots(1, 2)
obj1.z = 3  # Can add new attributes dynamically
print(obj1.z)  # 3

obj2 = WithSlots(1, 2)
# obj2.z = 3  # AttributeError: 'WithSlots' object has no attribute 'z'
print(obj2.x)  # 1
```

## 17. Metaclasses

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Add a class variable to every class created with this metaclass
        dct['class_id'] = id(cls)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.class_id)  # Some integer ID

# Another example: Singleton pattern using metaclass
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True (same instance)
```

## 18. Descriptors

```python
class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{self.name} must be between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(0, 150)

    def __init__(self, age):
        self.age = age

person = Person(25)
print(person.age)  # 25
# person.age = 200  # ValueError: age must be between 0 and 150
```

## 19. Mixins

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XMLMixin:
    def to_xml(self):
        xml = "<object>"
        for key, value in self.__dict__.items():
            xml += f"<{key}>{value}</{key}>"
        xml += "</object>"
        return xml

class Person(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.to_json())  # {"name": "Alice", "age": 30}
print(person.to_xml())   # <object><name>Alice</name><age>30</age></object>
```

## 20. Type Hints with Classes

```python
from typing import List, Optional, ClassVar

class Student:
    school_name: ClassVar[str] = "Python High"  # Class variable type hint

    def __init__(self, name: str, grades: List[int]) -> None:
        self.name: str = name
        self.grades: List[int] = grades
        self.mentor: Optional[str] = None

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def set_mentor(self, mentor_name: str) -> None:
        self.mentor = mentor_name

student = Student("Alice", [85, 90, 88])
print(student.average_grade())  # 87.66666666666667
student.set_mentor("Dr. Smith")
print(student.mentor)  # Dr. Smith
```

## 21. Operator Overloading (More Examples)

```python
class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j]
                       for j in range(len(self.data[0]))]
                       for i in range(len(self.data))])

    def __matmul__(self, other):  # @ operator
        return "Matrix multiplication result"

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = m1 + m2
print(m3)
# 6 8
# 10 12
print(m1 @ m2)  # Matrix multiplication result
```

## 22. Named Tuples (Class Alternative)

```python
from collections import namedtuple

# Creating a named tuple class
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
print(p1.x, p1.y)  # 10 20
print(p1[0], p1[1])  # 10 20

# Named tuples are immutable
# p1.x = 30  # AttributeError

# With defaults (Python 3.7+)
Point2 = namedtuple('Point2', ['x', 'y'], defaults=[0, 0])
p2 = Point2()
print(p2)  # Point2(x=0, y=0)
```

## 23. Enum Classes

```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Status(Enum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()

print(Color.RED)          # Color.RED
print(Color.RED.name)     # RED
print(Color.RED.value)    # 1
print(Color(1))           # Color.RED

for color in Color:
    print(color)
# Color.RED
# Color.GREEN
# Color.BLUE
```

## 24. Class Decorators

```python
def add_logging(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@add_logging
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)  # Creating instance of MyClass
```

## 25. Private Name Mangling in Inheritance

```python
class Parent:
    def __init__(self):
        self.__private = "Parent private"

    def get_private(self):
        return self.__private

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private = "Child private"

    def get_child_private(self):
        return self.__private

child = Child()
print(child.get_private())        # Parent private
print(child.get_child_private())  # Child private
# Both __private variables exist independently due to name mangling
print(child._Parent__private)     # Parent private
print(child._Child__private)      # Child private
```
