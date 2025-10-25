# Lesson 07 - Python Object-Oriented Programming (OOP)  <!-- omit in toc -->

This lesson covers object-oriented programming concepts in Python, including classes, inheritance, abstract classes, method overriding, and property decorators.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Basic Class Definition](#01-basic-class-definition)
  - [02. Inheritance and Method Overriding](#02-inheritance-and-method-overriding)
  - [03. Class Methods and Instance Methods](#03-class-methods-and-instance-methods)
  - [04. Abstract Base Classes](#04-abstract-base-classes)
  - [05. Complete Abstract Implementation](#05-complete-abstract-implementation)
  - [06. Property Decorators](#06-property-decorators)
- [OOP Design Patterns](#oop-design-patterns)
  - [Complete Property Pattern](#complete-property-pattern)
  - [Multiple Inheritance](#multiple-inheritance)
- [How to Run](#how-to-run)
- [Best Practices](#best-practices)
  - [1. **Class Design**](#1-class-design)
  - [2. **Inheritance Hierarchy**](#2-inheritance-hierarchy)
  - [3. **Encapsulation**](#3-encapsulation)
- [Practice Suggestions](#practice-suggestions)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand class definition and object instantiation
- Master inheritance and method overriding
- Learn about class methods and instance methods
- Understand abstract base classes and abstract methods
- Learn about private attributes and encapsulation
- Master property decorators for getter/setter patterns
- Develop object-oriented design skills

## Course Content

### 01. Basic Class Definition
**File:** `01/main.py`

Learn the fundamentals of class definition and object creation:

```python
#!/usr/bin/env python3

class Dog():
    def __init__(self, kind: str, name: str):
        '''
        The first step when creating a new object
        '''
        # Private attribute with double underscore
        self.__kind = kind
        self.name = name        # Public attribute
        self.legs = 4          # Public attribute

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('I can run by {} legs'.format(self.legs))

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
```

**Key Concepts:**
- `class` keyword for class definition
- `__init__()` method as constructor
- `self` parameter references current instance
- Private attributes with double underscore (`__attribute`)
- Public attributes (accessible directly)
- Instance methods that operate on object data
- Reference: [PEP 8 - Naming Styles](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

### 02. Inheritance and Method Overriding
**Files:** `02/animal.py`, `02/main.py`

Learn inheritance, method overriding, and private attribute access:

**Base Class (`02/animal.py`)**
```python
class Animal():
    def __init__(self, kind: str, name: str, legs: int):
        '''
        The first step when creating a new object
        '''
        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('no defined action')
```

**Derived Class (`02/main.py`)**
```python
#!/usr/bin/env python3

from animal import Animal
import sys
from typing import override

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        # Call parent constructor
        super().__init__(kind, name, 4)

    @override  # Good practice to indicate overriding
    def run(self):
        print('I can run by {} legs'.format(self.legs))

    def echo_kind(self):
        # This will fail - __kind is private to Animal
        print('I am {}.'.format(self.__kind))

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()

    try:
        # Will raise AttributeError
        puppy.echo_kind()
    except AttributeError as e:
        print('[Error]', e, file=sys.stderr)
```

**Key Concepts:**
- Class inheritance with `class Child(Parent):`
- `super()` function to call parent methods
- `@override` decorator from `typing` module
- Private attribute encapsulation (inaccessible from subclasses)
- Method overriding to customize behavior
- Exception handling for attribute access errors

### 03. Class Methods and Instance Methods
**Files:** `03/animal.py`, `03/main.py`

Learn the difference between class methods and instance methods:

**Class with Class Method (`03/animal.py`)**
```python
class Animal():
    def __init__(self, kind: str, name: str, legs: int):
        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):  # Instance method
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):    # Instance method
        print('no defined action')

    @classmethod      # Class method decorator
    def info(cls):
        print('This is Animal class.')
```

**Using Class Methods (`03/main.py`)**
```python
#!/usr/bin/env python3

from animal import Animal
import sys
from typing import override

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    @override
    def run(self):
        print('I can run by {} legs'.format(self.legs))

    @override
    @classmethod
    def info(cls):
        print('This is Dog class.')

if __name__ == '__main__':
    try:
        # This will fail - hello() needs an instance
        Animal.hello()
    except TypeError as e:
        print('[Error]', e, file=sys.stderr)

    # Class methods can be called on the class directly
    Animal.info()
    Dog.info()

    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
```

**Key Concepts:**
- `@classmethod` decorator for class methods
- `cls` parameter represents the class itself
- Class methods don't need instances to be called
- Instance methods require object instances
- Class method inheritance and overriding
- Reference: [Classmethod Documentation](https://docs.python.org/3/library/functions.html#classmethod)

### 04. Abstract Base Classes
**Files:** `04/animal.py`, `04/main.py`

Learn about abstract classes and methods:

**Abstract Base Class (`04/animal.py`)**
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Inherit from ABC
    def __init__(self, kind: str, name: str, legs: int):
        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):  # Concrete method
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    @abstractmethod   # Abstract method
    def run(self):
        raise NotImplementedError('Subclasses must implement abstract method')
```

**Failed Abstract Implementation (`04/main.py`)**
```python
#!/usr/bin/env python3

from animal import Animal
import sys

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    def run(self):  # Must implement abstract method
        print('I can run by {} legs'.format(self.legs))

class Bird(Animal):  # Missing run() implementation
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 2)

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()

    try:
        # This will fail - Bird doesn't implement run()
        eagle = Bird(kind='Sea Eagle', name='Andro')
        eagle.hello()
        eagle.run()
    except TypeError as e:
        print('[Error]', e, file=sys.stderr)
```

**Key Concepts:**
- `ABC` (Abstract Base Class) for creating abstract classes
- `@abstractmethod` decorator for abstract methods
- Subclasses must implement all abstract methods
- Cannot instantiate classes with unimplemented abstract methods
- Concrete methods can coexist with abstract methods
- Reference: [Abstract Base Classes](https://docs.python.org/3/library/abc.html)

### 05. Complete Abstract Implementation
**Files:** `05/animal.py`, `05/main.py`

Learn proper abstract method implementation:

**Complete Implementation (`05/main.py`)**
```python
#!/usr/bin/env python3

from animal import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    def run(self):  # Implement abstract method
        print('I can run by {} legs'.format(self.legs))

class Bird(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 2)

    def run(self):  # Implement abstract method
        print('I can jump by {} legs'.format(self.legs))

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()

    eagle = Bird(kind='Sea Eagle', name='Andro')
    eagle.hello()
    eagle.run()
```

**Key Concepts:**
- All subclasses must implement abstract methods
- Different implementations for different subclasses
- Polymorphism through common interface
- Abstract classes enforce implementation contracts

### 06. Property Decorators
**File:** `06/main.py`

Learn about property decorators for controlled attribute access:

```python
#!/usr/bin/env python3

class Dog():
    def __init__(self, kind: str, name: str):
        self.__kind = kind  # Private attribute
        self.name = name
        self.legs = 4

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('I can run by {} legs'.format(self.legs))

    @property
    def kind(self) -> str:
        '''
        Getter for private attribute __kind
        '''
        return self.__kind

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    print('I am a {}.'.format(puppy.kind))  # Access via property
```

**Key Concepts:**
- `@property` decorator creates getter methods
- Access private attributes through public interface
- Type hints with return annotations
- Property methods appear as attributes to users
- Encapsulation with controlled access

## OOP Design Patterns

### Complete Property Pattern
```python
class Dog:
    def __init__(self, kind: str):
        self.__kind = kind

    @property
    def kind(self) -> str:
        """Getter for kind"""
        return self.__kind

    @kind.setter
    def kind(self, value: str) -> None:
        """Setter for kind with validation"""
        if not value:
            raise ValueError("Kind cannot be empty")
        self.__kind = value

    @kind.deleter
    def kind(self) -> None:
        """Deleter for kind"""
        del self.__kind
```

### Multiple Inheritance
```python
class Walkable:
    def walk(self):
        print("Walking...")

class Swimmable:
    def swim(self):
        print("Swimming...")

class Duck(Animal, Walkable, Swimmable):
    def __init__(self, name: str):
        super().__init__("Duck", name, 2)
```

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-07/01
python3 main.py
```

```bash
cd lesson-07/02
python3 main.py
```

```bash
cd lesson-07/03
python3 main.py
```

```bash
cd lesson-07/04
python3 main.py
```

```bash
cd lesson-07/05
python3 main.py
```

```bash
cd lesson-07/06
python3 main.py
```

## Best Practices

### 1. **Class Design**
```python
# Good: Clear, single responsibility
class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    @property
    def balance(self) -> float:
        return self.__balance

# Avoid: Too many responsibilities
class BankAccountWithEverything:
    # Don't mix banking logic with UI, logging, etc.
    pass
```

### 2. **Inheritance Hierarchy**
```python
# Good: Logical inheritance
class Vehicle(ABC):
    @abstractmethod
    def start(self): pass

class Car(Vehicle):
    def start(self):
        print("Car started")

# Avoid: Deep inheritance chains
class A: pass
class B(A): pass
class C(B): pass  # Too deep
```

### 3. **Encapsulation**
```python
# Good: Controlled access
class Person:
    def __init__(self, age: int):
        self.__age = age

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        if 0 <= value <= 150:
            self.__age = value
        else:
            raise ValueError("Invalid age")

# Avoid: Direct access to everything
class Person:
    def __init__(self, age: int):
        self.age = age  # No validation
```

## Practice Suggestions

1. **Class Design**: Create classes for real-world entities (Car, Person, BankAccount)
2. **Inheritance**: Build hierarchies (Animal -> Mammal -> Dog)
3. **Abstract Classes**: Design interfaces for different implementations
4. **Properties**: Add validation and computed properties
5. **Polymorphism**: Use common interfaces with different implementations

## Related Resources

- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Data Model Documentation](https://docs.python.org/3/reference/datamodel.html#basic-customization)
- [Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Property Decorator](https://docs.python.org/3/library/functions.html#property)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [PEP 318 - Decorators](https://www.python.org/dev/peps/pep-0318/)