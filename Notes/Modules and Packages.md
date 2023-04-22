### Modules and Packages

Modules are files containing Python code, while packages are collections of modules organized in a directory hierarchy. They help in organizing your code and reusing functionality across projects.

#### Importing a Module

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

#### Importing a Specific Function or Variable from a Module

```python
from math import sqrt

print(sqrt(16))  # Output: 4.0
```

#### Aliasing a Module or Function

```python
import math as m

print(m.sqrt(16))  # Output: 4.0

from math import sqrt as square_root

print(square_root(16))  # Output: 4.0
```

#### Creating a Package

To create a package, organize your modules into a directory hierarchy and include an `__init__.py` file in each directory.

For example, create a package named `my_package` with the following structure:

```
my_package/
    __init__.py
    my_module.py
```

You can then import and use the package in your code:

```python
from my_package import my_module

my_module.my_function()
```

These are the basics of functions, function arguments, modules, and packages in Python. They help you create reusable code and organize your projects efficiently. For more information, please refer to the official Python documentation.