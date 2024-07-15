# Python Generators

> Generators is a general software programming concept, and is not Python exclusive.

- In Python, an iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets. Python iterators implement the iterator design pattern, which allows you to traverse a container and access its elements. The iterator pattern decouples the iteration algorithms from container data structures.
- In summary, an iterator will yield each item or value from a collection or a stream of data while doing all the internal bookkeeping required to maintain the state of the iteration process.
- Generator functions are special types of functions that *allow you to create iterators using a functional style*. Unlike regular functions, which typically compute a value and return it to the caller, generator functions return a generator iterator that yields a stream of data one value at a time.

> When a generator function is compiled they become an object that supports an iteration protocol. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


```python
# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)
```

## Generators in depth: Next and Iter functions

A key to fully understanding generators is the next() function and the iter() function.
- The next() function allows us to access the next element in a sequence. Lets check it out:

  ```python
  def simple_gen():
      for x in range(3):
          yield x

  print(next(g))
  >>> 0
  ```

- The python iter function is used to return an iterator for the object. Before continue,lets rememebr that eechnically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
- Therefore, The iter() is used to create an object that supports the iteration protocol, and per example be compatible with next() function:

  ```python
  hello_string = "hello"
  hello_s_iterable = iter(hello_string)
  #now we are able to use next()
  next(hello_s_iterable) #will output h
  next(hello_s_iterable) #will output e
  ```
> Internally when we iterate over an iterable object, we are calling the next function to retrieve the next value. Note that next function is only supported over iterable objects

## Python Gencomp - Generator Comprehension

> [Python provides a sleek syntax for defining a simple generator in a single line of code; this expression is known as a generator comprehension. The following syntax is extremely useful and will appear very frequently in Python code](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Creating-your-own-generator:-generator-comprehensions)


A generator comprehension is the lazy version of a list comprehension. It is just like a list comprehension except that it returns an iterator instead of the list ie an object with a next() method that will yield the next element.

> The Gencomp Expression allows us to create a generator without the yield keyword.

```python
# List Comprehension 
list_comprehension = [i for i in range(11) if i % 2 == 0] 

print(list_comprehension) 


# Generator Expression 
generator_expression = (i for i in range(11) if i % 2 == 0) 
  
print(generator_expression) 
```


## Difference vs Regular Function

Generator functions will automatically suspend and resume their execution and state around the last point of value generation

In few and practical worlds, when we call a generator funcion, the don't actually return a value and and then exists, instead they return a value and hold an "state", and on a next call it may return the following value.

# Advantages

> TLDR; memory eficient.

The advantage is that instead of having to compute an entire series of values up front, the generator computes one value waits until the next value is called for.

> For example, *the range() function doesn't produce an list in memory for all the values from start to stop*. Instead it just keeps track of the last number and the step size, to provide a flow of numbers.

# Resources

- https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Creating-your-own-generator:-generator-comprehensions
- https://www.w3schools.com/python/python_iterators.asp
- https://realpython.com/python-iterators-iterables/