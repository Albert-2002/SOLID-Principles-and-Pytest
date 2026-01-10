# Object-Oriented Programming (OOP) in Python — Complete Guide

This guide teaches **classes and object-oriented programming in Python**, from basics to advanced features and Python-specific syntax.

---

## 1. What Is OOP in Python?

Object-Oriented Programming is a paradigm where programs are built using **objects**, which bundle:

- **Data** (attributes)
- **Behavior** (methods)

Python is a **multi-paradigm language**, but it has **very powerful and flexible OOP support**.

---

## 2. Classes and Objects

### Defining a Class

```python
class Person:
    pass
```

### Creating Objects (Instances)

```python
p1 = Person()
p2 = Person()
```

---

## 3. Attributes and Methods

### Instance Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

```python
p = Person("Alice", 30)
print(p.name)
print(p.age)
```

### Instance Methods

```python
class Person:
    def greet(self):
        print(f"Hi, I'm {self.name}")
```

---

## 4. The `__init__` Constructor

- Automatically called when an object is created
- Initializes object state

```python
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
```

---

## 5. Class Attributes vs Instance Attributes

```python
class Dog:
    species = "Canine"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

```python
Dog.species
```

---

## 6. Encapsulation and Access Control

Python uses **conventions**, not strict enforcement.

### Public

```python
self.name
```

### Protected (convention)

```python
self._age
```

### Private (name mangling)

```python
self.__salary
```

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary
```

---

## 7. Properties (`@property`)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
```

---

## 8. Inheritance

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
```

```python
d = Dog()
d.speak()
```

---

## 9. Method Resolution Order (MRO)

```python
class A: pass
class B(A): pass
class C(B): pass

print(C.mro())
```

Python uses **C3 linearization**.

---

## 10. Multiple Inheritance

```python
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass
```

---

## 11. Polymorphism

```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

animals = [Cat(), Dog()]
for a in animals:
    print(a.speak())
```

---

## 12. Duck Typing (Python-Specific)

> "If it quacks like a duck, it's a duck"

```python
def make_sound(animal):
    animal.speak()
```

---

## 13. Composition (Preferred Over Inheritance)

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```

---

## 14. Class Methods and Static Methods

### Class Methods

```python
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
```

### Static Methods

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

---

## 15. Magic (Dunder) Methods

### Common Dunder Methods

```python
__init__
__str__
__repr__
__len__
__eq__
__lt__
__add__
```

### Example

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

---

## 16. Operator Overloading

```python
v1 + v2
v1 == v2
v1 < v2
```

---

## 17. Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## 18. Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

---

## 19. Slots (Memory Optimization)

```python
class Person:
    __slots__ = ('name', 'age')
```

---

## 20. Metaclasses (Advanced)

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

---

## 21. Mixins

```python
class JsonMixin:
    def to_json(self):
        return self.__dict__
```

---

## 22. Object Lifecycle

```python
__new__
__init__
__del__
```

---

## 23. Best Practices

- Prefer composition over inheritance
- Keep classes small
- Avoid deep inheritance trees
- Use `@dataclass` when possible
- Make objects immutable when appropriate

---

## 24. When NOT to Use OOP

- Simple scripts
- Pure data pipelines
- Performance-critical numeric code

---

## 25. Summary

Python OOP is:

- Dynamic
- Flexible
- Convention-based
- Extremely powerful

Mastering it requires understanding **both syntax and design principles**.

---

If you want next steps, I can:

- Add **exercises with solutions**
- Teach **design patterns in Python**
- Show **real-world OOP projects**
- Compare **OOP vs FP in Python**
