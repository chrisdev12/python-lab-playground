# TLDR; ABC vs Protocol

> Python offers two ways to define code interfaces: Abstract Base Classes (ABC), which use Nominal Typing, and Protocol, which uses Structural Typing. Nominal Typing relies on class hierarchies to define relationships clearly, such as a RandomForestModel being a type of Model, making connections between classes explicit. On the other hand, Protocol is at the heart of Python’s duck typing philosophy. It allows any class that implements certain methods to be compatible, even without an explicit declaration, meaning a RandomForestModel just needs to act like a Model to be considered one - https://fmind.medium.com/make-your-mlops-code-base-solid-with-pydantic-and-pythons-abc-aeedfe9c3e65

> Choosing between these two does impact the design of your software - https://www.youtube.com/watch?v=dryNwWvSd4M&ab_channel=ArjanCodes

> Abstract Base Classes (ABC) and protocol classes are both ways of defining interfaces in Python. The main difference between them is that with ABCs, you typically use inheritance, whereas with protocols, that's not necessary because they rely on something called duck typing.


# Nominal vs structural subtyping

- Nominal subtyping is strictly based on the class hierarchy. If class Dog inherits class Animal, it’s a subtype of Animal. Instances of Dog can be used when Animal instances are expected. This form of subtyping is what Python’s type system predominantly uses: it’s easy to understand and produces clear and concise error messages, and matches how the native isinstance check works – based on class hierarchy.

- Structural subtyping is based on the operations that can be performed with an object. Class Dog is a structural subtype of class Animal if the former has all attributes and methods of the latter, and with compatible types.

- Structural subtyping can be seen as a static equivalent of duck typing, which is well known to Python programmers. See PEP 544 for the detailed specification of protocols and structural subtyping in Python.

> In duck typing, the behaviors and properties of an object determine the object type, not the explicit type of the object. 
>
> The duck typing is inspired by the duck test: If it walks like a duck and its quacks like a duck, then it must be a duck.
>
> In practice, when you write a function that accepts input, you care more about the behaviors and properties of the input, not its explicit type.

- PEP 544 (The reason to introduce protocols): Structural subtyping is natural for Python programmers since it matches the runtime semantics of duck typing: an object that has certain properties is treated independently of its actual runtime class. However, as discussed in PEP 483, both nominal and structural subtyping have their strengths and weaknesses. Therefore, in this PEP we do not propose to replace the nominal subtyping described by PEP 484 with structural subtyping completely. Instead, protocol classes as specified in this PEP complement normal classes, and users are free to choose where to apply a particular solution. See section on rejected ideas at the end of this PEP for additional motivation.


# Protocols vs ABC - Introducing ABC

- ABC have been part of the Python standard library for a long time. In comparision to Protocols, that have been added in Python 3.8.

- The dedicated module abc allows creating abstract classes and declaring abstract methods to organize structure for our data models within the project.

*Advantage:*

- The advantage of defining abstract classes is that we create a blueprint of a common interface, in this case the interface is a set of methods. Therefore, all child classes must implement mentioned functions. This allows us to take advantage of the polymorphism mechanism and program other parts of code to an interface not an implementation.

*Understaing the Disadvantages:* 


- Due to the inheritance nature of Abstract Classes promotes the child classes be much dependent on their parent classes.
  - On one hand, this is just what we wanted in the first place – straightforward inheritance, on the other hand, we strengthened coupling in our code, making classes, objects and methods more dependent on each other. 
  - Python interpreter has created a relation between parent and child classes based on inheritance stated in the definition 

- Last and probably most critical issue is the fact that each part of the code requires a specified interface as an input. For instance, the function feeding_time() only uses the feed() method of the Animal Abstract class but right now it has to accept the whole object as a parameter. Our example is fairly simple, but imagine that the parent class implements more than 10 methods – most of the functionalities provided in the input interface (the Animal object) would basically become redundant in the scope of this function. **We could potentially separate Animal into smaller classes but it would unnecessarily complicate our code design.**

> Try to keep Interfaces well-delimited promots the Interfaces Segregation principle.

```python
class Animal(ABC):

    @abstractmethod
    def say_hello(self):
        pass
    
    @abstractmethod
    def feed(self):
        pass

def feeding_time(animal: Animal):
    print("Preparing food...")
    animal.feed()
    print("Food served!")
```
- Luckily, there is a way to solve these issues as well as organize and simplify our code, reduce coupling and loose dependencies in existing files. The solution is called “Protocols”.


# Introducing Protocols - ¿What is a Protocol in Python?

>  The term protocols is used for types supporting structural subtyping - https://peps.python.org/pep-0544/

- Protocols are not a new concept, even in Python. Introduced in version 3.8 as an alternative to Abstract Base Classes, they rely on structural typing. In this mechanism, Python interpreter checks the structure of the object (its methods, attributes etc.) to determine whether it can be used in a specific function/class and the types match. This strategy, based on comparing objects and checking their types, has a specific name in dynamically typed languages (such as Python): duck typing. It follows a very simple rule:

> If it walks like a duck and it quacks like a duck, then it must be a duck.

- It means that if two objects have the same methods and attributes, Python will treat them as the same type. For comparison, ABCs use nominal typing, where object relationship is defined by inheritance stated deliberately in our class definition (e.g. class B(A)). 

- To continue the comparission, a protocol is a set of methods or attributes that an object must have in order to be considered compatible with that protocol. Protocols enable you to define interfaces without explicitly creating a class or inheriting from a specific base class.

- *Protocols are, therefore, interfaces which help define what is expected as an input of our methods. Hopefully, by using them we might be able to avoid problems mentioned before and improve our code design.*

> Protocols are primarily used for type hinting and static type checking. You can use a protocol as a type annotation to indicate that an argument or variable must conform to a specific protocol; allowing you to create interfaces without the need for explicit inheritance.


# Defining a Implementing a Protocol

Protocols are defined using the typing.Protocol class or the typing.Protocol decorator:

```python
from typing import Protocol

class Printable(Protocol):
    def print(self) -> None:
        pass
```
In this example, we define a protocol named Printable that requires an object to have a print method. The Protocol class allows you to define abstract methods (in this case, just print) that must be implemented by objects conforming to the protocol.

**To implement a protocol, you don't need to explicitly declare it. Instead, you can ensure that an object conforms to a protocol by implementing the required methods. Here's an example:**

```python
class Book:
    def __init__(self, title: str):
        self.title = title

    def print(self) -> None:
        print(f"Book Title: {self.title}")

# type annotation to indicate that an argument or variable must conform to a specific protocol
def print_object(obj: Printable) -> None:
    obj.print()

```
## Multiple Protocols

- You can also define a protocol that combines multiple other protocols. Here's an example: We define a protocol named Serializable with a serialize method. Then we define another protocol named PrintableAndSerializable that combines both the Printable and Serializable protocols.

```python
class Serializable(Protocol):
    def serialize(self) -> str:
        pass

class PrintableAndSerializable(Printable, Serializable):
    pass
```

# When to use which one ?

- ABCs are particularly useful when you already want to have a bit of implementation in your base class.
- Use Protocols when you do not need or want to include inheritance in your code. However get in mind that they're not as well integrates as ABCs in terms of predictability, due to its structural subtyping nature and how python analyze it at runtime. Per example, if we just want to specify what type of argument a function expects in terms of what kind of this object should look like.


# Resources
- https://www.youtube.com/watch?v=dryNwWvSd4M&ab_channel=ArjanCodes
- https://peps.python.org/pep-0544/
- https://typing.readthedocs.io/en/latest/spec/protocol.html
- https://dev.to/shameerchagani/what-is-a-protocol-in-python-3fl1
- https://idego-group.com/blog/2023/02/21/we-need-to-talk-about-protocols-in-python/
- https://fmind.medium.com/make-your-mlops-code-base-solid-with-pydantic-and-pythons-abc-aeedfe9c3e65