# Dependency managment & Packaging Managment

First, some quick definitions: packaging refers to the general activity of creating and distributing Python packages, which are bundles of Python code (usually as a compressed file archive) in a particular format that can be distributed to other people and installed by a tool like pip. The action of turning your Python source code into the package thing is often referred to as building the package.

There are many other activities that are not packaging but are related, such as virtual environment management and dependency management. Most of this post will not be about those topics, but they will turn up later when we discuss popular tools that handle packaging and these other things.

For example, one of the most common doubts -at least mine- was [the difference between setuptools - setup.py and requirements.txt](https://stackoverflow.com/questions/43658870/requirements-txt-vs-setup-py)


- The short answer is that requirements.txt is for listing package requirements only. setup.py on the other hand is more like an installation script. If you don't plan on installing the python code, typically you would only need requirements.txt.

- The file setup.py describes, in addition to the package dependencies, the set of files and modules that should be packaged (or compiled, in the case of native modules (i.e., written in C)), and metadata to add to the python package listings (e.g. package name, package version, package description, author, ...).

- This typical question in the python community serves as a starting point, because setuptools with its setup.py is more related to the packaging process, while requirements.txt is aimed at managing the dependencies that the project uses. At some point both interact, but by design they are different (see the sections below for a more detailed explanation of each).

> *Because both files list dependencies, this can lead to a bit of duplication, but their design purposes are different*

>Note: You would normally execute pip and setup.py from a sandbox, such as those created with the program venv. This will avoid installing python packages outside the context of your project's development environment.

---

### Requirements.txt


- This file lists python package requirements. It is a plain text file (optionally with comments) that lists the package dependencies of your python project (one per line). 

- *It does not describe the way in which your python package is installed*. You would generally consume the requirements file with pip install -r requirements.txt.

- The filename of the text file is arbitrary, but is often requirements.txt by convention.

- If multiplerequirements-X.txt variants are present, then usually one will list runtime dependencies, and the other build-time, or test dependencies. Some projects also cascade their requirements file, i.e. when one requirements file includes another file (example). Doing so can reduce repetition.

### Setup.py

> setup.py became famous for being part of setuptools, what was once the de-facto standard for creating packages in Python, and what it will do is known as the concept of Build backends which is explained in detail in a section below.

> **setup.py:** helps you to create packages that you can redistribute. The setup.py script is meant to install your package on the end user's system, not to prepare the development environment as pip install -r requirements.txt does. [See this answer for more details on setup.py.](https://stackoverflow.com/questions/1471994/what-is-setup-py)


- This is a python script which uses the setuptools module to define a python package.

- When a python user does pip install ./pkgdir_my_module (or pip install my-module), pip will run setup.py in the given directory (or module). Similarly, any module which has a setup.py can be pip-installed, e.g. by running pip install . from the same folder.

- Do I really need both? Short answer is no, but it's nice to have both. They achieve different purposes, but they can both be used to list your dependencies.


## Dependency managment Installing packages 

> pip has become the de-facto and blessed installer tool (for Python packages not otherwise provided by your platform's package manager) either in- or outside of virtual environments (virtualenv or pyvenv).

> all this section info was mainly inspired in https://packaging.python.org/en/latest/guides/tool-recommendations/

pip is the standard tool to install packages from PyPI. You may want to read pip’s recommendations for secure installs. Pip is available by default in most Python installations through the standard library package ensurepip.

Alternatively, consider pipx for the specific use case of installing Python applications that are distributed through PyPI and run from the command line. Pipx is a wrapper around pip and venv that installs each application into a dedicated virtual environment. This avoids conflicts between the dependencies of different applications, and also with system-wide applications making use of the same Python interpreter (especially on Linux).


Do not use easy_install (part of Setuptools), which is deprecated in favor of pip (see pip vs easy_install for details). Likewise, do not use python setup.py install or python setup.py develop, which are also deprecated (see Is setup.py deprecated? for background and How to modernize a setup.py based project? for migration advice).

## Manage dependencies version through lock files

pip-tools and Pipenv are two recognized tools to create lock files, which contain the exact versions of all packages installed into an environment, for reproducibility purposes.

TODO; put more info about it




# Packaging management in Python Projects

- The basics of Python Packaging in early 2023: https://drivendata.co/blog/python-packaging-2023
- Configuring metadata: https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata
- Generating distribution archives: https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives
- A fundamental concept/tool in Python Packaging Management -and the one that theoretically makes it possible- is the **Build Backend** concept. Tools like pip and build do not actually convert your sources into a distribution package (like a wheel); that job is performed by a **Build Backend**. The build backend determines how your project will specify its configuration, including metadata (information about the project, for example, the name and tags that are displayed on PyPI) and input files. Build backends have different levels of functionality, such as whether they support building extension modules, and you should choose one that suits your needs and preferences.


## Packaging managment - What is a build backend

> [Tools like pip and build do not actually convert your sources into a distribution package (like a wheel); that job is performed by a build backend.](https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-a-build-backend)

> [Build backen in few workds it is some Python library that does the package building.](https://drivendata.co/blog/python-packaging-2023)

PEP 517 introduced the distinct concepts of build "frontends" and build "backends". The backend is the program that reads your pyproject.toml and actually does the work of turning your source code into a package archive that can be installed or distributed. The frontend is just a user interface (usually a command-line program) that calls the backend.

- Examples of frontends include: pip, build, poetry, hatch, pdm, flit

- Examples of backends include: setuptools (>=61), poetry-core, hatchling, pdm-backend, flit-core


The design of separating these two pieces in the build workflow means that—in principle—you can mix and match frontends and backends. Under this design, when you do pip install pointed at source code (e.g., local source or a tar.gz source distribution), or when you run a command like python -m build or poetry build, you are using a frontend. That frontend looks up which build backend you declared in your pyproject.toml (step #1 of the above how-to section), makes a fresh virtual environment by default, installs the backend into the virtual environment, and runs it to build your package. Once again, backends that work this way are called "PEP 517 backends".

> Build backend is a library that takes a source tree and builds a source distribution or built distribution from it. The build is delegated to the backend by a frontend. All backends offer a standardized interface. Examples of build backends are flit’s flit-core, hatch’s hatchling, Maturin, meson-python, scikit-build-core, and Setuptools.

## Packaging Management - Choosing a build backend

> [Choosing a build backend official doc](https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-a-build-backend)


Popular build backends for pure-Python packages include, in alphabetical order:

- Flit-core – developed with but separate from flit. A minimal and opinionated build backend. It does not support plugins.

- Hatchling – developed with but separate from hatch. Supports plugins.

- PDM-backend – developed with but separate from pdm. Supports plugins.

- Poetry-core – developed with but separate from poetry. Supports plugins.

    - Unlike other backends on this list, Poetry-core does not support the standard [project] table (it uses a different format, in the [tool.poetry] table).

- Setuptools, which used to be the only build backend. Supports plugins. (setuptools use the wide famous [setup-py file](https://stackoverflow.com/questions/1471994/what-is-setup-py))

> Look more opinions around this stuff at https://stackoverflow.com/questions/71080546/what-is-the-preferred-way-to-develop-a-python-package-without-using-setup-py

> Modern packaging question: [pyproject.toml, setup.cfg, setup.py. What's the difference?](https://www.reddit.com/r/learnpython/comments/yqq551/pyprojecttoml_setupcfg_setuppy_whats_the/)

### Setuptools - Common Build Backends

> If you use setuptools, please be aware that some features that predate standardisation efforts are now deprecated and only temporarily kept for compatibility.
>
> In particular, do not use direct python setup.py invocations. On the other hand, configuring setuptools with a setup.py file is still fully supported, although it is recommended to use the modern [project] table in pyproject.toml (or setup.cfg) whenever possible and keep setup.py only if programmatic configuration is needed. See Is setup.py deprecated?.
>
> Other examples of deprecated features you should not use include the setup_requires argument to setup() (use the [build-system] table in pyproject.toml instead), and the easy_install command (cf. pip vs easy_install).


- [Example of a creating a local package with setuptools](https://pkiage.hashnode.dev/creating-a-local-python-package-in-a-virtual-environment#heading-3-setup-package-configuration)

- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#configuring-your-project

- https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

- [setup.py vs setup.cfg](https://stackoverflow.com/questions/39484863/whats-the-difference-between-setup-py-and-setup-cfg-in-python-projects)

- Now going forward and as of PEP-517 and PEP-518, you may have to use a pyproject.toml in order to specify that you want to use setuptools as the build-tool and an additional setup.cfg file to specify the details. For more details you can read the article [setup.py vs setup.cfg in Python](https://towardsdatascience.com/setuptools-python-571e7d5500f2).


### But wait… I always found info that says: "instead of setup.py, use pip" does it mean that setup.py is deprecated ?

> The info in this section was extracted from [this source](https://packaging.python.org/en/latest/discussions/setup-py-deprecated). More info about setuptools state of art could be found there too.

No, setup.py and Setuptools are not deprecated.

Setuptools is perfectly usable as a build backend for packaging Python projects. And setup.py is a valid configuration file for Setuptools that happens to be written in Python, instead of in TOML for example (a similar practice is used by other tools like nox and its noxfile.py configuration file, or pytest and conftest.py).

However, python setup.py and the use of setup.py as a command line tool are deprecated.

*This means that commands such as the following MUST NOT be run anymore*:

- python setup.py install
- python setup.py develop
- python setup.py sdist
- python setup.py bdist_wheel

---

# Resources

- https://packaging.python.org/en/latest/guides/tool-recommendations/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
- https://stackoverflow.com/questions/43658870/requirements-txt-vs-setup-py
- https://stackoverflow.com/questions/71080546/what-is-the-preferred-way-to-develop-a-python-package-without-using-setup-py
- https://www.reddit.com/r/learnpython/comments/yqq551/pyprojecttoml_setupcfg_setuppy_whats_the/


## resources- Package managment
- https://drivendata.co/blog/python-packaging-2023
- https://www.reddit.com/r/Python/comments/16qz8mx/pipenv_piptools_pdm_or_poetry/

## Resources - setuptools
- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
- https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
- https://packaging.python.org/en/latest/discussions/setup-py-deprecated/
- https://stackoverflow.com/questions/1471994/what-is-setup-py