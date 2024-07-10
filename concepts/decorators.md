# Python Decorators

> Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. - [Geeks For Gekks](https://www.geeksforgeeks.org/decorators-in-python/)

> A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are typically applied to functions, and they play a crucial role in enhancing or modifying the behavior of functions. - [DataCamp](https://www.datacamp.com/tutorial/decorators-python)

- Decorators are used to modify the behaviour of function or class. Through Decorators, We are able to add some new capabilitites to an existing function, without the need to add that extra code.
-**¿How works?**: In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
- **Some technical background**: Decorators are possible in Python because of how Python treats functions as *first-class citizens, which makes it possible to implement patterns such as high-order-function*, which a Decorator theoretically could be considered.

> Functions in Python are first class citizens. This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable. This property is crucial as it allows functions to be treated like any other object in Python, enabling greater flexibility in programming - [DataCamp](https://www.datacamp.com/tutorial/decorators-python)


> Decorators provide a simple syntax for calling higher-order functions. - [RealPython](https://realpython.com/primer-on-python-decorators/)

```python
def new_decorator(original_function):
  def wrap_func():
    print('some extra code, before the original function')
    original_function()
    print('some extra code, after the original function')

  return wrap_func

@new_decorator
def simple_function():
  return "something"

#the @ syntax is sugar syntatic of (and looks nicer IMO, but it is not black magic though)
new_decorator(simple_function)
```

> Decorators is not an exclusive Python concept, it could be found too in Languages as JS

# Resources

- https://realpython.com/primer-on-python-decorators/
- https://www.datacamp.com/tutorial/decorators-python
- https://www.geeksforgeeks.org/decorators-in-python/
- https://peps.python.org/pep-0318/