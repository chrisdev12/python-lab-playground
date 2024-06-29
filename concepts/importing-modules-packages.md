# What is a package in Python?

Before diving into the details of __init__.py files, it's important to understand what a package is in Python. A package is a way to organize related modules (Python files) into a single, easy-to-use namespace. Packages allow you to group related functionality together, making it easier to organize and reuse your code.

A package in Python is simply a directory that contains a special file called __init__.py. The __init__.py file is executed when the package is imported, and it can contain any Python code you like.

# What is the meaning of __init__.py files?
The __init__.py file has several meanings in Python. First and foremost, it is used to mark a directory as a package. When the Python interpreter encounters a directory that contains an __init__.py file, it treats the directory as a package and allows you to import modules from that package using the dot notation.

Secondly, the __init__.py file is used to initialize the package. This means that you can use the __init__.py file to set up any configuration or state that is needed by the package. For example, you can define package-level variables or import other modules that the package depends on.

Finally, the __init__.py file is used to control what symbols are exported from the package. When you import a module from a package, Python looks for the symbol in the module first, and then in the package's __init__.py file. This allows you to selectively import symbols from the package without cluttering up the namespace.

## Why are __init__.py files needed?
__init__.py files are needed for several reasons. First and foremost, they allow you to organize your code into logical units called packages. This makes it easier to manage and reuse your code, and it also helps to avoid naming conflicts.

Secondly, __init__.py files are needed to control the import behavior of a package. By selectively importing symbols from a package, you can avoid name clashes and keep your code organized.

Finally, __init__.py files are often used to set up package-level configuration and state. This can include defining package-level variables or importing other modules that the package depends on.

> https://www.youtube.com/watch?v=GxCXiSkm6no&ab_channel=NeuralNine (Good example of the use of __init__.py file)


# How Python handles modules.

When you start the interpreter with a script, this script becomes the main module, with the matching name __main__.

When using import, other modules are searched in the search path, that you can also access (and change) using sys.path. The first entry of sys.path is usually empty and stands for the current directory.

- https://stackoverflow.com/questions/22942650/relative-import-from-init-py-file-throws-error 
- https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#69099298


# Import errors: “attempted relative import with no known parent package” 

- Error fixed with sys.path.append("..")
- [Virtual envs](./virtual-envs.md), as is explain at https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944
- Directory structure that favor how python handles the modules: https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#69099298 
- [Using launch.json in VsCode](https://www.youtube.com/watch?v=Ad-inC3mJfU&t=21s&ab_channel=k0nze) -> This is a suboptimal solution that works locally, and forces anyone that works on this project to use vscode as their IDE. The best solution is to package the extern directory as its own package and have it part of the requirements for the project, and then you can import it from there. Unfortunately, you are trying to fix an anti-pattern by promoting another one.

## Import errors - solution examples

- https://www.youtube.com/watch?v=nk7UWUKlfGM&ab_channel=chinamatt (solution of relative imports using setup tools to enable abosule imports )
- https://www.youtube.com/watch?v=lR-OKnX7uOw&ab_channel=TheDevLife (Solution of relative imports using the sys.path.append)


# Resources

## resources - init_py
- https://www.geeksforgeeks.org/what-is-__init__-py-file-in-python/
- https://stackoverflow.com/questions/448271/what-is-init-py-for
- https://sentry.io/answers/what-is-init-py-for-in-python/
- https://www.youtube.com/watch?v=cONc0NcKE7s&ab_channel=EricOMeehan
- https://martinxpn.medium.com/what-are-packages-in-python-and-what-is-the-role-of-init-py-files-82-100-days-of-python-325a992b2b13
- https://stackoverflow.com/questions/9439480/from-import-vs-import
- https://www.youtube.com/watch?v=GxCXiSkm6no&ab_channel=NeuralNine (Good example of the use of __init__.py file)

## resources - relative import errors

- https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
- https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800
- https://stackoverflow.com/questions/22942650/relative-import-from-init-py-file-throws-error (Explanation of how Python handles modules and why the ValueError: Attempted relative import in non-package happens)
- https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944 (Tired of sys.path hacks)
