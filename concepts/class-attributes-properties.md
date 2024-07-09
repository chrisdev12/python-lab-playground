# Understanding Variables, Attributes, and Properties

- Variables: A variable is a name that refers to a value. Variables can hold any type of object.

- Attributes: An attribute is a value associated with an object. Attributes can be accessed using the dot notation.

- Properties: Properties in Python are special methods that act like attributes. They are created using the @property decorator to define a method as an attribute, providing additional functionality like getters, setters, and deleters.

> Usually the term variable of a class is used when referring to class attributes, this can lead to confusion, because not all use that name, and could led to be confused with instance attributes too.

# Class attributes & Instance attributes

> TLDR; class attributes remain the same for every object and are defined outside the __init__() function. Instance attributes are somewhat dynamic because they can have different values in each object.

When creating a class in Python, you'll usually create attributes that may be shared across every object of a class or attributes that will be unique to each object of the class. 

As an object-oriented language, Python provides two scopes for attributes: class attributes and instance attributes. 


- To give a basic definition of both terms, class attributes are class variables that are inherited by every object of a class. The value of class attributes remain the same for every new object. (class attributes are defined outside the __init__() function.)

- On the other hand, instance attributes, which are defined in the __init__() function, are class variables that allow us to define different values for each object of a class.

```python
class Student:
    school = "freeCodeCamp.org"
    
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John
```
> In the example above, The school variable acts as a class attribute while name and course are instance attributes

> For Java or C++ programmers, the class attribute is similar—but not identical—to the static member. We’ll see how they differ later. Look the differences -related to python namespaces- [here](https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide) 


# Beware of mutability in class attributes

> If you’re just using a class variable to assign a default value to a would-be Python instance variable, don’t use mutable values. A good options would be stuck to instance attributes entirely, as demonstrated in the introduction.

What if your class attribute has a mutable type? You can manipulate the class attribute by accessing it through a particular instance and, in turn, end up manipulating the referenced object that all instances are accessing (as pointed out by Timothy Wiseman).

This is no good—altering our Python class variable via one instance alters it for all the others!


```python
s1 = Service(['a', 'b'])
s2 = Service(['c', 'd'])

s1.data.append(1)

s1.data
## [1]
s2.data
## [1]

s2.data.append(2)

s1.data
## [1, 2]
s2.data
## [1, 2]
```

> The theorical explanation is that at the namespace level all instances of Service are accessing and modifying the same list in Service.__dict__ without making their own data attributes in their instance namespaces.


> Python class variables have their place within the school of good code. When used with care, they can simplify things and improve readability. But when carelessly thrown into a given class, they’re sure to trip you up.


## Class attributes common Practice

The normal practice in Python is to exposure the attributes directly. A property can be added later if additional actions are required when getting or setting.

Most of the modules in the standard library follow this practice. Public variables (not prefixed with an underscore) typically don't use property() unless there is a specific reason (such as making an attribute read-only).


> Python doesn't have private variables at all, it has a kind of convention where a private class instance attribute is considered private if the name is prefixed with __<name>, but it is not the same level of access modifiers that exists in other languages

> Python doesn’t have the notion of access modifiers, such as private, protected, and public, to restrict access to attributes and methods. In Python, the distinction is between public and non-public class members.
>
>If you want to signal that a given attribute or method is non-public, then you have to use the well-known Python convention of prefixing the name with an underscore (_). That’s the reason behind the naming of the attributes ._x and ._y.
>
>Note that this is just a convention. It doesn’t stop you and other programmers from accessing the attributes using dot notation, as in obj._attr. However, it’s bad practice to violate this convention.

# Python Properties

> Get the deep info in this article: https://realpython.com/python-property

With Python’s property(), you can create managed attributes in your classes. You can use managed attributes, also known as properties, when you need to modify their internal implementation without changing the public API of the class. Providing stable APIs can help you avoid breaking your users’ code when they rely on your classes and objects.

Properties are arguably the most popular way to create managed attributes quickly and in the purest Pythonic style.

- Properties represent an intermediate functionality between a plain attribute (or field) and a method. In other words, they allow you to create methods that behave like attributes. With properties, you can change how you compute the target attribute whenever you need to do so.

- Programming languages such as Java and C++ encourage you to never expose your attributes to avoid this kind of problem. Instead, you should provide getter and setter methods, also known as accessors and mutators, respectively. These methods offer a way to change the internal implementation of your attributes without changing your public API.

- [Python’s property() is the Pythonic way to avoid formal getter and setter methods in your code.](https://realpython.com/python-property/#getting-started-with-pythons-property)

- Property can be used as a function, but its best known and most widely used version is as a decorator.

```python
# Read-only attributes
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
```

# Resources

- https://www.freecodecamp.org/news/python-attributes-class-and-instance-attribute-examples/
- https://builtin.com/software-engineering-perspectives/python-attributes
- https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
- https://realpython.com/python-property/