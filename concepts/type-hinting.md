# What and Why Type Hinting in Python ?
 
> Type hints help you build and maintain a cleaner architecture. The act of writing type hints forces you to think about the types in your program. While the dynamic nature of Python is one of its great assets, being conscious about relying on duck typing, overloaded methods, or multiple return types is a good thing.

- Python is a dynamically-typed language in which you can code without giving a second thought to data types until runtime–which is one of the features that make Python particularly beginner-friendly.

- However, this dynamic nature can also lead to bugs that are difficult to debug, especially in large codebases or complex data processing pipelines, where the data flow might not be immediately obvious.

- Type hinting is the formal solution to **statically** indicate the type of a value within your Python code. It was specified in PEP 484 and introduced in Python 3.5.

Here’s an example of adding type information to a function. You annotate the arguments and the return value:

```python
def greet(name: str) -> str:
    return "Hello, " + name
```

- The *name: str* syntax indicates the name argument should be of type str. 
- The *() -> str* syntax indicates the greet() function will return a string.

## Type Hinting Advantages

- **Improved code readability**: Type hints act as a form of documentation that helps developers understand the types of arguments a function expects and what it returns. This enhanced clarity makes the code more readable and easier to understand.

- **Error detection**: Tools like 'pyright' and mypy can be used to statically analyze your Python code. It checks the consistency of types in your code based on the type hints and alerts you about type-related errors before runtime. Learn why the Dagster team recommends skipping mypy entirely and just using pyright.

- **Better IDE support**: Many Integrated Development Environments (IDEs) and linters can utilize type hints to provide better code completion, error checking, and refactoring.

- **Facilitates large-scale projects**: For larger projects with multiple developers, type hints can be very beneficial in understanding the structure and flow of data throughout the codebase. We’ve published a guide on how to include and maintain type annotations for public Python projects.

## Limitations

**Not enforced at runtime**: Python's type hints are not enforced but are merely hints, and the Python interpreter will not raise errors if the provided types do not match the actual values. This might lead to a misconception that type hints can enforce type safety, which they cannot.

**Over-complicated**: For small or simple scripts, type hints might seem like an overkill, and could potentially complicate code that should be straightforward and simple.

# kinds of types

> As in other similar solutions such as Typescript, in Python the type hinting is made up of several types

Take an in-depth look at:
- https://dagster.io/blog/python-type-hinting
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

# The typing module

> This module provides runtime support for type hints. The most fundamental support consists of the types Any, Union, Callable, TypeVar, and Generic. For a full specification, please see PEP 484. For a simplified introduction to type hints, see PEP 483.


- This module module contains many more composite types, including Counter, Deque, FrozenSet, NamedTuple, and Set. In addition, the module includes other kinds of types that you’ll see in later sections.


# Resources
- https://thepythoncodingbook.com/2022/12/27/type-hints-in-python-functions/
- https://dagster.io/blog/python-type-hinting
- https://realpython.com/lessons/type-hinting/
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- https://www.reddit.com/r/Python/comments/17dpmll/are_you_using_types_in_python/
- https://docs.python.org/3/library/typing.html
- https://realpython.com/python-type-checking/