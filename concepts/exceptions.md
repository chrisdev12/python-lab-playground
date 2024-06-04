# What are exceptions ?

> Exceptions are a general Programming concept, it isn't Python exclusive. However, their implementation details do vary compared to other languages.

- An exception represents an error or indicates that something is going wrong. Some programming languages, such as C, and Go, encourage you to return error codes, which you check. In contrast, Python encourages you to raise exceptions, which you handle.
- They allow you to handle errors and exceptional situations in your code.

> In Python, not all exceptions are errors. The built-in StopIteration exception is an excellent example of this. Python internally uses this exception to terminate the iteration over iterators. Python exceptions that represent errors have the Error suffix attached to their names.
>
>Python also has a specific category of exceptions that represent warnings to the programmer. Warnings come in handy when you need to alert the user of some condition in a program. However, that condition may not warrant raising an exception and terminating the program. A common example of a warning is DeprecationWarning, which appears when you use deprecated features.


# When Python will raise an exception ?

When a problem occurs in a program, Python automatically raises an exception. For example, watch what happens if you try to access a nonexistent index in a list object:

```python
>>> colors = [
...     "red",
...     "orange",
...     "yellow",
...     "green",
...     "blue",
...     "indigo",
...     "violet"
... ]

>>> colors[10]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

```
> In the example above, Python raised the exception on its own, which it’ll only do with built-in exceptions. You, as a programmer, have the option to raise built-in or custom exceptions, as you’ll learn in the section Choosing the Exception to Raise: Built-in vs Custom.

- Every raised exception has a traceback, also known as a stack trace, stack traceback, or backtrace, among other names. A traceback is a report containing the sequence of calls and operations that traces down to the current exception.

- To raise an exception by yourself, you’ll use the [raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) statement, which has the following general syntax:

# How raise an exception in my code ?

- In Python, you can raise either *built-in* or *custom exceptions*. When you raise an exception, the result is the same as when Python does it. You get an exception traceback, and your program crashes unless you handle (as is explained in the try-catch below section) the exception on time.

```python
> raise [expression [from another_expression]]

> raise Exception("Error message here.")
```

## Choosing the Exception to Raise: Built-in vs Custom

When it comes to manually raising exceptions in your code, deciding which exception to raise is an important step. In general, you should raise exceptions that clearly communicate the problem you’re dealing with. In Python, you can raise two different kinds of exceptions:

- Built-in exceptions: These exceptions are built into Python. You can use them directly in your code without importing anything.

- User-defined exceptions: Custom exceptions are those that you create when no built-in exception fits your needs. You’ll typically put them in a dedicated module for a specific project.
In the following sections, you’ll find some guidelines for deciding which exception to raise in your code

### Raising Built-in Exceptions

Python has a rich set of built-in exceptions structured in a class hierarchy with the BaseException class at the top. One of the most frequently used subclasses of BaseException is Exception.

The Exception class is a fundamental part of Python’s exception-handling scaffolding. It’s the base class for most of the built-in exceptions that you’ll find in Python. It’s also the class that you’ll typically use to create your custom exceptions.

Python has more than sixty [built-in]( https://docs.python.org/3/library/exceptions.html#built-in-exceptions) exceptions. You’ve probably seen some of the following concrete exceptions in your day-to-day coding:

> Built in exception are typically throwed by Python, but could be raised by the User too

In most cases, you’ll likely find an appropriate built-in exception for your specific use case. If that’s your case, then favor the built-in exception over a custom one. For example, say you’re coding a function to compute the square of all the values in an input list, and you want to ensure that the input object is a list or tuple:

```python
>>> def squared(numbers):
...     if not isinstance(numbers, list | tuple):
...         raise TypeError(
...             f"list or tuple expected, got '{type(numbers).__name__}'"
...         )
...     return [number**2 for number in numbers]
...

>>> squared([1, 2, 3, 4, 5])
[1, 4, 9, 16, 25]

>>> squared({1, 2, 3, 4, 5})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in squared
TypeError: list or tuple expected, got 'set'
```

### Raising custom Exceptions
> If you don’t find a built-in exception that semantically suits your needs, then you can define a custom one.

- To raise a custom exception you first must inherit from another exception class, typically Exception. 
-  For example, say that you’re coding a gradebook app and need to calculate the students’ average grades. You want to ensure that all the grades are between 0 and 100. To handle this scenario, you can create a custom exception called GradeValueError. You’ll raise this exception if a grade value is outside the target interval, meaning it’s invalid:

```python
# grades.py

class GradeValueError(Exception):
    pass

def calculate_average_grade(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            raise GradeValueError(
                "grade values must be between 0 and 100 inclusive"
            )
        total += grade
        count += 1
    return round(total / count, 2)

```
- In this example, you first create a custom exception by inheriting from Exception. You don’t need to add new functionality to your custom exception, so you use the pass statement to provide a placeholder class body. This new exception is specific to your grade project. Note how the exception name helps communicate the underlying issue.

# Handling Exception with try-catch

- Exceptions will cause your program to terminate unless you handle them using a try … except block.
- If your code raises an exception in a function but doesn’t handle it there, then the exception propagates to where you called function. If your code doesn’t handle it there either, then it continues propagating until it reaches the main program. If there’s no exception handler there, then the program halts with an exception traceback.


```python
>>> try:
...     colors[10]
... except IndexError:
...     print("Your list doesn't have that index :-(")
... else
...     print("do it if try is executed with no errors")
... finally:
...     print("Finally statement: it will be always executed")

> Your list doesn't have that index :-(
> Finally statement: it will be always executed

```
When dealing with some Python code bases *it is not always clear what kind of exceptions might occur*, so it is important to take advantage of Python's ability to deal with multiple exceptions, *putting them in order from the most specific to the most general. This will ensure that all exceptions are caught by the most appropriate handler.*

```python
def divide_by_zero():
    return 1/0 # will fail and raise a ZeroDivisionError

try:
    divide_by_zero()
    raise Exception("My custom exception.")
except ValueError as e:
    print(f"Caught value error: {repr(e)}")
except Exception as e:
    print(f"Caught custom exception: {repr(e)}")

```

**What is the intended use of the optional "else" clause of the "try" statement in Python?**

- The else statement runs if there are no exceptions and if not interrupted by a return, continue, or break statement.

- [The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try...except statement.](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

- So, if you have a method that could, for example, throw an IOError, and you want to catch exceptions it raises, but there's something else you want to do if the first operation succeeds, and you don't want to catch an IOError from that operation, you might write something like this:

```python
try:
    operation_that_can_throw_ioerror()
except IOError:
    handle_the_exception_somehow()
else:
    # we don't want to catch the IOError if it's raised
    another_operation_that_can_throw_ioerror()
finally:
    something_we_always_need_to_do()
```
> There is one big reason to use else - style and readability. It's generally a good idea to keep code that can cause exceptions near the code that deals with them.

# Explicit Exception chaining - Introducing Python "raise from" usage


- implicit chaining with explicit raise EXCEPTION or implicit raise (__context__ attribute);
- explicit chaining with explicit raise EXCEPTION from CAUSE (__cause__ attribute).

**Motivation to introduce explicit chaining**

- During the handling of one exception (exception A), it is possible that another exception (exception B) may occur. In today’s Python (version 2.4), if this happens, exception B is propagated outward and exception A is lost. In order to debug the problem, it is useful to know about both exceptions. The __context__ attribute retains this information automatically.

- Sometimes it can be useful for an exception handler to intentionally re-raise an exception, either to provide extra information or to translate an exception to another type. The __cause__ attribute provides an explicit way to record the direct cause of an exception.

- When you use from, the __cause__ attribute is set and the message states that the exception was directly caused by. If you omit the from then no __cause__ is set, but the __context__ attribute may be set as well, and the traceback then shows the context as during handling something else happened.

*raise EXCEPTION from CAUSE* is equivalent to 

```python
exc = EXCEPTION
exc.__cause__ = CAUSE
raise exc
```

In the following example, a database provides implementations for a few different kinds of storage, with file storage as one kind. The database designer wants errors to propagate as DatabaseError objects so that the client doesn’t have to be aware of the storage-specific details, but doesn’t want to lose the underlying error information.

```python
class DatabaseError(Exception):
    pass

class FileDatabase(Database):
    def __init__(self, filename):
        try:
            self.file = open(filename)
        except IOError, exc:
            raise DatabaseError('failed to open') from exc
```

- If the call to open() raises an exception, the problem will be reported as a DatabaseError, with a __cause__ attribute that reveals the IOError as the original cause.

## Enhanced reporting in the chained exceptions

The default exception handler will be modified to report chained exceptions. The chain of exceptions is traversed by following the __cause__ and __context__ attributes, with __cause__ taking priority. In keeping with the chronological order of tracebacks, the most recently raised exception is displayed last; that is, the display begins with the description of the innermost exception and backs up the chain to the outermost exception. The tracebacks are formatted as usual, with one of the lines:

> The above exception was the direct cause of the following exception:

or

> During handling of the above exception, another exception occurred:

depending whether they are linked by __cause__ or __context__ respectively. Here is a sketch of the procedure:

```python
def print_chain(exc):
    if exc.__cause__:
        print_chain(exc.__cause__)
        print '\nThe above exception was the direct cause...'
    elif exc.__context__:
        print_chain(exc.__context__)
        print '\nDuring handling of the above exception, ...'
    print_exc(exc)
```
**Examples of the reporting**

```python
>>> try:
...   open("database.sqlite")
... except OSError:
...   raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error

```
- To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause: 
```python 
raise RuntimeError from exc
```

```python
>>> try:
...    func()
... except ConnectionError as exc:
...    raise RuntimeError('Failed to open database') from exc

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database

```

> Look more info in https://stackoverflow.com/questions/24752395/python-raise-from-usage

# Deciding when to raise Exceptions

- Signal errors and exceptional situations: The most common use case of the raise statement is to signal that an error or exceptional situation has occurred. When an error or exceptional situation occurs in your code, you can raise an exception in response.

- Reraise exception after doing some additional processing: A common use case of raise is to reraise an active exception after performing some operations. A good example of this use case is when you need to log the error before raising the actual exception.

# Raising Exception Groups

```python
>>> raise ExceptionGroup(
...     "several errors",
...     [
...         ValueError("invalid value"),
...         TypeError("invalid type"),
...         KeyError("missing key"),
...     ],
... )
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  | ExceptionGroup: several errors (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | ValueError: invalid value
    +---------------- 2 ----------------
    | TypeError: invalid type
    +---------------- 3 ----------------
    | KeyError: 'missing key'
    +------------------------------------

```
# Following Best Practices When Raising Exceptions

- **Favor specific exceptions over generic ones**: You should raise the most specific exception that suits your needs. This practice will help you track down and fix problems and errors.

- **Provide informative error messages and avoid exceptions with no message**: You should write descriptive and explicit error messages for all your exceptions. This practice will provide a context for those debugging the code.

- **Favor built-in exceptions over custom exceptions**: You should try to find an appropriate built-in exception for every error in your code before writing your own exception. This practice will ensure consistency with the rest of the Python ecosystem. Most experienced Python developers will be familiar with the most common built-in exceptions, making it easier for them to understand and work with your code.

- **Avoid raising the AssertionError exception**: You should avoid raising the AssertionError in your code. This exception is specifically for the assert statement, and it’s not appropriate in other contexts.

- **Raise exceptions as soon as possible**: You should check error conditions and exceptional situations early in your code. This practice will make your code more efficient by avoiding unnecessary processing that a delayed error check could throw away. This practice fits the fail-fast design.

- **Explain the raised exceptions in your code’s documentation**: You should explicitly list and explain all the exceptions that a given piece of code could raise. This practice helps other developers understand which exceptions they should expect and how they can handle them appropriately.



# Resources - Get deep info here
- https://realpython.com/python-raise-exception/
- https://docs.python.org/3/library/exceptions.html#built-in-exceptions
- https://sentry.io/answers/raise-an-exception-in-python/
- https://www.freecodecamp.org/espanol/news/sentencias-try-y-except-de-python-como-menejar-excepciones-en-python/
- https://stackoverflow.com/questions/855759/what-is-the-intended-use-of-the-optional-else-clause-of-the-try-statement-in
- https://docs.python.org/3/tutorial/errors.html#exception-chaining