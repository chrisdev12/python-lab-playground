# What and Why of Interfaces & Abstract classes ?

- Interface defines the inputs and outputs of a thing, and don't specify the implementation of it.

- Abstract classes not only define inputs and the inputs, it also could provide an implementation.

- However, beyond the difference around the implementation, the similarities between interface and conrete classes are much more important than the differences. Mainly because both share a main goal: abstraction (central in Objected Oriented Programming).

- At a high level, an interface acts as a blueprint for designing classes. Like classes, interfaces define methods. Unlike classes, these methods are abstract. An abstract method is one that the interface simply defines. It doesn’t implement the methods. This is done by classes, which then implement the interface and give concrete meaning to the interface’s abstract methods. They are just defined but not implemented rather they require subclasses for implementation.

- Abstraction play an important role in software engineering. As an application grows, updates and changes to the code base become more difficult to manage. More often than not, you wind up having classes that look very similar but are unrelated, which can lead to some confusion. In this tutorial, you’ll see how you can use a Python interface to help determine what class you should use to tackle the current problem.

> The advantage of defining abstract classes is that we create a blueprint of a common interface, in this case the interface is a set of methods. Therefore, all child classes must implement mentioned functions. This allows us to take advantage of the polymorphism mechanism and program other parts of code to an interface not an implementation

# Implementing these abstractions in Python

> Python does not come with Interfaces and Abstract classes by default due to its nature as an interpreted language

> Interfaces are not necessary in Python. This is because Python has proper multiple inheritance, and also ducktyping, which means that the places where you must have interfaces in Java, you don't have to have them in Python.
>
> That said, there are still several uses for interfaces. Some of them are covered by Pythons Abstract Base Classes, introduced in Python 2.6. They are useful, if you want to make base classes that cannot be instantiated, but provide a specific interface or part of an implementation.

- Taking into account the nature of the language and the tools through which interfaces and abstract classes can be implemented in Python, it is important to note that the conceptual differentiation between interface and abstract class becomes tribal in practice. In conceptual terms, if we do not offer any implementation we can talk about an interface, and in case we do we could talk about an Abstract Class, but this is not really important, even from conceptual boundary perspective becase the central goal should always be to promote abstraction.


- In any case the module that allows us to easily implement it is called ABC, which is an acronym for Abstract Base Class, this is clarified here to avoid further confusion.


- Python’s approach to interface design is somewhat different when compared to languages like Java, Go, and C++. These languages all have an interface keyword, while Python does not. Python further deviates from other languages in one other aspect. It doesn’t require the class that’s implementing the interface to define all of the interface’s abstract methods.


# Informal Interfaces

In certain circumstances, you may not need the strict rules of a formal Python interface. Python’s dynamic nature allows you to implement an informal interface. An informal Python interface is a class that defines methods that can be overridden, but there’s no strict enforcement.

In the following example, you’ll take the perspective of a data engineer who needs to extract text from various different unstructured file types, like PDFs and emails. You’ll create an informal interface that defines the methods that will be in both the PdfParser and EmlParser concrete classes:

```python
 class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass
```

InformalParserInterface defines the two methods .load_data_source() and .extract_text(). These methods are defined but not implemented. The implementation will occur once you create concrete classes that inherit from InformalParserInterface.

*As you can see, InformalParserInterface looks identical to a standard Python class. You rely on duck typing to inform users that this is an interface and should be used accordingly.*

> Note: Haven’t heard of duck typing? This term says that if you have an object that looks like a duck, walks like a duck, and quacks like a duck, then it must be a duck! To learn more, check out Duck Typing.

With duck typing in mind, you define a classe that implement the InformalParserInterface. To use your interface, you must create a concrete class. A concrete class is a subclass of the interface that provides an implementation of the interface’s methods. You’ll create two concrete classes to implement your interface. The first is PdfParser, which you’ll use to parse the text from PDF files:

```python
class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass
```
Such informal interfaces are fine for small projects where only a few developers are working on the source code. However, as projects get larger and teams grow, this could lead to developers spending countless hours looking for hard-to-find logic errors in the codebase!

# Formal interfaces & Abstract classes

Informal interfaces can be useful for projects with a small code base and a limited number of programmers. However, informal interfaces would be the wrong approach for larger applications. In order to create a formal Python interface, you’ll need a few more tools from Python’s abc module.

## Using ABC option to create formal interfaces/ abstract classes

> What is the ABC of Python? It stands for the abstract base class and is a concept in Python classes based on abstraction. Abstraction is an integral part of object-oriented programming.


To enforce the subclass instantiation of abstract methods, you’ll utilize Python’s builtin *ABC module*

1. A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:

```python
from abc import ABC

class MyABC(ABC):
    pass
```
2. Note that the type of ABC is still ABCMeta, therefore inheriting from ABC requires the usual precautions regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the metaclass keyword and using ABCMeta directly, for example:

```python
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass
```

## Practical example with ABC

But let's look at a concrete example continuing with our remote control example. We can see how the @abstractmethod decorator is used.

An abstract method is a method that does not have an implementation, that is to say, that does not carry code. A method defined with this decorator will force the classes that implement this interface to code it.

```python
from abc import abstractmethod
from abc import ABCMeta

class Mando(metaclass=ABCMeta):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def upVolume(self):
        pass

    @abstractmethod
    def bajar_v

    # Defining a concrete method
    def required_concrete_method(self):
        print("Calling concrete method")
```
> An abstract class can only be defined but cannot be instantiated because of the fact that they are not a concrete class. Python doesn’t allow creating objects for abstract classes because there is no actual implementation to invoke rather they require subclasses for implementation.


# Resources

- https://ellibrodepython.com/abstract-base-class
- https://geekpython.in/abc-in-python
- https://realpython.com/python-interface/
- https://stackoverflow.com/questions/2124190/how-do-i-implement-interfaces-in-python
- https://www.reddit.com/r/Python/comments/12jghhf/interfaces_in_python/
- https://docs.python.org/3/library/abc.html