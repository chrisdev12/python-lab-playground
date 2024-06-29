# What & Why of the if __name__ == "__main__" pattern in Python

> In Python, if __name__ == '__main__' is a common construct that is often used to make a module both importable and executable. The if __name__ == '__main__'  construct is a conditional statement that checks whether the current script is being run as the main program or if it is being imported as a module by another script. - https://rs-punia.medium.com/what-does-if-name-main-mean-in-python-fa6b0460a62d

```python
#foo.py

print ("Always executed")
 
if __name__ == "__main__": 
    print ("Executed Foo.py when invoked directly")
else: 
    print ("Executed when imported foo.py")
```


Short Answer

> It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module - https://realpython.com/if-name-main-python/

Before executing a program, the Python interpreter assigns the name of the Python module into a special variable called __name__. Depending on whether you are executing the program through the command line or importing the module into another module, the assignment for __name__ will vary.

Therefore, this name main syntax is a boilerplate code that protects users from accidentally invoking the script when they didn't intend to. Here are some common problems when the guard is omitted from a script:


- If you import the guardless script in another script (e.g. import my_script_without_a_name_eq_main_guard), then the latter script will trigger the former to run at import time and using the second script's command line arguments. This is almost always a mistake.

- If you have a custom class in the guardless script and save it to a pickle file, then unpickling it in another script will trigger an import of the guardless script, with the same problems outlined in the previous bullet.


> All of the code that is at indentation level 0 gets executed. Functions and classes that are defined are, well, defined, but none of their code gets run. Unlike other languages, there's no main() function that gets run automatically - the main() function is implicitly all the code at the top level.


> Long answer explanation: https://stackoverflow.com/questions/419163/what-does-if-name-main-do highest score answer

## Why Does It Work This Way?
You might naturally wonder why anybody would want this. Well, sometimes you want to write a .py file that can be both used by other programs and/or modules as a module, and can also be run as the main program itself. Examples:

  - Your module is a library, but you want to have a script mode where it runs some unit tests or a demo.

  - Your module is only used as a main program, but it has some unit tests, and the testing framework works by importing .py files like your script and running special test functions. You don't want it to try running the script just because it's importing the module.

  - Your module is mostly used as a main program, but it also provides a programmer-friendly API for advanced users.

Beyond those examples, it's elegant that running a script in Python is just setting up a few magic variables and importing the script. "Running" the script is a side effect of importing the script's module.


# Resources
- https://realpython.com/if-name-main-python/
- https://rs-punia.medium.com/what-does-if-name-main-mean-in-python-fa6b0460a62d
- https://stackoverflow.com/questions/419163/what-does-if-name-main-do
- https://builtin.com/articles/name-python#:~:text=__name__
- https://www.freecodecamp.org/espanol/news/python-if-name-main/


