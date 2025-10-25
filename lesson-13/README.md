# Lesson 13 - Python Modules and Package Development

This lesson covers Python module organization, package development, and distribution from basic single-file modules to professional packages with proper structure and testing.

## Learning Objectives

- Understand Python module and package concepts
- Learn module organization and import strategies
- Master package structure and `__init__.py` usage
- Create distributable packages with `pyproject.toml`
- Understand build systems and package management
- Learn professional package development workflow
- Master testing in package context

## Course Content

### 01. Basic Module Organization
**Files:** `01/animal.py`, `01/mammalia.py`, `01/main.py`

Learn basic module organization with separate files:

**Base Animal Class (`01/animal.py`)**
```python
class Animal():

    def __init__(self, kind: str, name: str, legs: int):
        '''
        The first step when creating a new object
        '''

        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('no defined action')
```

**Specialized Classes (`01/mammalia.py`)**
```python
from typing import override
from animal import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    @override
    def run(self):
        print('I can run by {} legs'.format(self.legs))
```

**Main Application (`01/main.py`)**
```python
#!/usr/bin/env python3

from mammalia import Dog

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
```

**Key Concepts:**
- Direct module imports (`from animal import Animal`)
- Module-level organization
- `@override` decorator for method overriding
- Private attributes with double underscore (`__kind`)

### 02. Package Structure with __init__.py
**Files:** `02/main.py`, `02/animal/__init__.py`, `02/animal/base.py`, `02/animal/mammalia.py`

Learn proper package organization with `__init__.py`:

**Package Initialization (`02/animal/__init__.py`)**
```python
from .mammalia import Dog

__all__ = ['Dog']
```

**Base Classes (`02/animal/base.py`)**
```python
class Animal():

    def __init__(self, kind: str, name: str, legs: int):
        '''
        The first step when creating a new object
        '''

        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('no defined action')
```

**Specialized Classes (`02/animal/mammalia.py`)**
```python
from typing import override
from .base import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    @override
    def run(self):
        print('I can run by {} legs'.format(self.legs))
```

**Main Application (`02/main.py`)**
```python
#!/usr/bin/env python3

from animal.mammalia import Dog

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
```

**Key Concepts:**
- Package directory with `__init__.py`
- Relative imports (`.base`, `.mammalia`)
- `__all__` for controlling public API
- Hierarchical package structure

### 03. Professional Package Development
**Files:** `03/pyproject.toml`, `03/src/animal/`, `03/tests/`, `03/examples/`

Learn professional package development with modern tools:

**Project Configuration (`03/pyproject.toml`)**
```toml
[build-system]
requires = [
    "hatchling"
]
build-backend = "hatchling.build"

[project]
name = "animal"
description = "A simple animal package"
readme = "README.md"
requires-python = ">=3.12"
classifiers = [
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Python :: 3.15",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows :: Windows 11",
]
dynamic = [
    "version"
]

[project.license]
text = "MIT"

[[project.authors]]
name = "Author Name"
email = "user@example.com"

[project.urls]
Homepage = "https://example.com/"
Registry = "https://example.com/"

[project.optional-dependencies]
dev = ["pytest"]

[tool.hatch.build.targets.sdist]
include = ["src/animal"]

[tool.hatch.build.targets.wheel]
packages = ["src/animal"]

[tool.hatch.version]
path = "src/animal/__about__.py"

[tool.pytest.ini_options]
log_cli = false
log_cli_level = "INFO"
minversion = "8.4"
pythonpath = ["src"]
testpaths = ["tests"]
```

**Version Management (`03/src/animal/__about__.py`)**
```python
VERSION='0.1.0'
```

**Package Initialization (`03/src/animal/__init__.py`)**
```python
from .mammalia import Dog

__all__ = ['Dog']
```

**Test Cases (`03/tests/test_mammalia.py`)**
```python
#!/usr/bin/env python3

from animal.mammalia import Dog

def test_dog():
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
```

**Usage Example (`03/examples/main.py`)**
```python
#!/usr/bin/env python3

from animal.mammalia import Dog

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
```

**Key Concepts:**
- `src/` layout for better isolation
- `pyproject.toml` for modern Python packaging
- Hatchling as build backend
- Dynamic versioning
- Separate test and example directories
- pytest configuration

## Package Development Concepts

### Module vs Package
- **Module**: Single Python file (`.py`)
- **Package**: Directory containing `__init__.py` and other modules
- **Namespace Package**: Package without `__init__.py` (PEP 420)

### Import Strategies

#### Absolute Imports
```python
from mypackage.submodule import MyClass
import mypackage.submodule.another
```

#### Relative Imports
```python
from .submodule import MyClass      # Same package
from ..parent import ParentClass    # Parent package
from ...grandparent import GClass   # Grandparent package
```

#### Import Patterns
```python
# Direct import
from animal import Dog

# Module import
import animal
dog = animal.Dog('Shiba', 'Maru')

# Selective import
from animal import Dog, Cat

# Aliased import
from animal import Dog as Puppy
```

### Package Structure Patterns

#### Flat Layout
```
myproject/
├── mypackage/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
├── setup.py
└── README.md
```

#### Src Layout (Recommended)
```
myproject/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
├── tests/
├── pyproject.toml
└── README.md
```

### __init__.py Patterns

#### Simple Re-export
```python
from .module1 import Class1
from .module2 import Class2

__all__ = ['Class1', 'Class2']
```

#### Lazy Loading
```python
def __getattr__(name):
    if name == "expensive_module":
        from . import expensive_module
        return expensive_module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
```

#### Version Information
```python
from .__about__ import __version__
from .core import MainClass

__all__ = ['MainClass', '__version__']
```

## Modern Python Packaging

### pyproject.toml Structure

#### Build System
```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"
```

#### Project Metadata
```toml
[project]
name = "my-package"
description = "A great package"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "you@example.com"},
]
keywords = ["example", "tutorial"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
dynamic = ["version"]
dependencies = [
    "requests>=2.20",
    "click>=8.0",
]
```

#### Optional Dependencies
```toml
[project.optional-dependencies]
dev = ["pytest", "black", "flake8"]
docs = ["sphinx", "sphinx-rtd-theme"]
test = ["pytest>=6.0", "pytest-cov"]
```

#### Entry Points
```toml
[project.scripts]
my-tool = "mypackage.cli:main"

[project.gui-scripts]
my-gui = "mypackage.gui:main"
```

### Build Backends

#### Hatchling (Recommended)
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/mypackage"]
```

#### Setuptools
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
```

#### Poetry
```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "my-package"
version = "0.1.0"
```

## How to Run Examples

### Basic Module Example
```bash
# Navigate to corresponding directory
cd lesson-13/01
python3 main.py
```

### Package Structure Example
```bash
cd lesson-13/02
python main.py
```

### Professional Package Development
```bash
cd lesson-13/03

# Install development dependencies
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Run example
python3 examples/main.py

# Build the package
python3 -m build
```

## Package Development Workflow

### 1. Project Setup
```bash
# Create project structure
mkdir mypackage
cd mypackage
mkdir src/mypackage tests examples docs

# Initialize files
touch src/mypackage/__init__.py
touch src/mypackage/__about__.py
touch pyproject.toml
touch README.md
touch requirements.txt
```

### 2. Development Cycle
```bash
# Install in development mode
pip install -e .

# Make changes to source code
# Run tests
pytest

# Update version
# Build package
python3 -m build

# Upload to PyPI (optional)
twine upload dist/*
```

### 3. Testing Strategy
```python
# Unit tests
def test_basic_functionality():
    assert function() == expected_result

# Integration tests
def test_package_import():
    import mypackage
    assert hasattr(mypackage, 'main_function')

# Example tests
def test_examples():
    from examples.main import main
    main()  # Should not raise exceptions
```

## Best Practices

### 1. **Use Src Layout**
```
# Good: src layout
myproject/
├── src/
│   └── mypackage/
│       └── __init__.py
└── tests/

# Avoid: flat layout can cause import issues
myproject/
├── mypackage/
│   └── __init__.py
└── tests/
```

### 2. **Clear __init__.py**
```python
# Good: Explicit public API
from .core import MainClass
from .utils import helper_function

__all__ = ['MainClass', 'helper_function']
__version__ = "1.0.0"

# Avoid: Importing everything
from .core import *  # Unclear what's public
```

### 3. **Proper Relative Imports**
```python
# Good: Use relative imports within package
from .base import BaseClass
from ..utils import utility_function

# Avoid: Absolute imports for internal modules
from mypackage.base import BaseClass  # Fragile
```

### 4. **Version Management**
```python
# Good: Single source of truth
# __about__.py
__version__ = "1.0.0"

# __init__.py
from .__about__ import __version__

# Avoid: Hardcoded versions in multiple places
```

### 5. **Configuration Management**
```toml
# Good: Use pyproject.toml
[project]
name = "mypackage"
dynamic = ["version"]

# Avoid: setup.py for new projects
# Use setup.py only for complex build requirements
```

## Advanced Package Features

### Entry Points and Console Scripts
```toml
[project.scripts]
mytool = "mypackage.cli:main"

[project.entry-points."mypackage.plugins"]
plugin1 = "mypackage.plugins:Plugin1"
```

### Package Data and Resources
```toml
[tool.hatch.build.targets.wheel]
include = [
    "src/mypackage",
    "src/mypackage/data/*.txt",
]
```

```python
# Accessing package data
from importlib import resources

def load_data():
    with resources.open_text("mypackage.data", "config.txt") as f:
        return f.read()
```

### Namespace Packages
```python
# No __init__.py in namespace package
# mycompany/
#   package1/
#     __init__.py
#   package2/
#     __init__.py

# Usage
from mycompany.package1 import feature1
from mycompany.package2 import feature2
```

## Common Issues and Solutions

### Import Errors
```python
# Problem: ModuleNotFoundError
# Solution: Check PYTHONPATH and package structure

# Problem: Circular imports
# Solution: Restructure code or use lazy imports

# Problem: Relative import in script
# Solution: Use absolute imports or run as module
python3 -m mypackage.script
```

### Build Issues
```bash
# Problem: Package not found after installation
# Check pyproject.toml packages configuration

# Problem: Missing files in distribution
# Check include/exclude patterns in build configuration

# Problem: Version not updating
# Check dynamic version configuration
```

## Practice Suggestions

1. **Convert Script to Package**: Take existing scripts and organize into packages
2. **Create CLI Tools**: Build command-line tools with entry points
3. **Plugin Systems**: Design extensible applications with plugin entry points
4. **Library Development**: Create reusable libraries for common tasks
5. **Package Templates**: Create project templates for consistent structure
6. **Documentation Integration**: Add Sphinx documentation to packages

## Related Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 518 - Build System Requirements](https://peps.python.org/pep-0518/)
- [PEP 621 - Metadata in pyproject.toml](https://peps.python.org/pep-0621/)
- [Hatchling Documentation](https://hatch.pypa.io/latest/)
- [PyPI - Python Package Index](https://pypi.org/)
- [Python Module Documentation](https://docs.python.org/3/tutorial/modules.html)