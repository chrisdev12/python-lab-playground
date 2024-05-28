# What are virtual classes in Python ?

> What is a virtual base class: Imagine that although Friend does not explicitly inherit from Person, it implements .name() and .age(), so Person becomes a virtual base class of Friend
>
> The key difference between these and standard subclasses is that virtual base classes use the .__subclasscheck__() dunder method to implicitly check if a class is a virtual subclass of the superclass. Additionally, virtual base classes don’t appear in the subclass MRO.

```python
class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'age') and 
                callable(subclass.age))
    
    lass Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def name(self):
        pass

    def age(self):
        pass
    
```
# Practical uses of virtual classes

I read Interfaces in Python: Protocols and ABCs and it gives me a better understanding. We have duck typing in Python:

> If it talks and walks like a duck, then it is a duck.

However, a Bird and Aeroplane both can fly(). But they are not the same thing. Hence, we need to define an interface to distinguish them from each other. (Python does not have an interface keyword, so we are actually using abstract classes)

Let's me show an example:

We have Duck and MyPlane in our program. Both of them implemented fly() method. Now we want to choose a plane from the hangar, get some people on board, and fly to another city. Apparently, we cannot put people onto a Duck, so we define an interface called (actually, an abstract class) Plane. And we let MyPlane to subclass Plane.

Everything works fine. When we want to choose a plane, we check if it subclasses Plane. However, the Boeing company developed a package, which has a Boeing747Plane. We bought the plane (from boeing_airplanes import Boeing747Plane), but it is not recognized as a plane. It does have a fly() method, but it's not inherited from our Plane class so our Python interpreter won't recognize it as a plane.

The good news is that Python is a flexible language. Thanks for register method of ABCMeta, after we do Plane.register(Boeing747Plane), Boeing747Plane is a subclass of Plane now. We can use third-party Boeing747Plane like our own built Plane. Hooray!

So you see, virtual classes are used when we want to make a class from a third-party package to be a subclass of our own abstract class. We want it to implement our interface, but we cannot change its code, so we tell the interpreter explicitly "it implemented our interface, please treat it as the subclass of our own class". I think normally we wouldn't want to use it, but when you need to, use it cautiously. As Luca Cappelletti said, this is one of many flexibilities that Python allows for, following its philosophy of "we are adults here".


# Resources 
- https://stackoverflow.com/questions/51666120/whats-the-usage-of-a-virtual-subclass