# Lesson 14 - Command Line Argument Processing  <!-- omit in toc -->

This lesson covers comprehensive command-line argument processing in Python using argparse (built-in), docopt (declarative), and Click (modern) frameworks, from basic argument parsing to professional CLI application development and distribution.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. argparse - Built-in Argument Parsing](#01-argparse---built-in-argument-parsing)
  - [02. docopt - Declarative Argument Parsing](#02-docopt---declarative-argument-parsing)
  - [03. Packaged CLI Tool with Entry Points](#03-packaged-cli-tool-with-entry-points)
  - [04. Modern CLI with Click Framework](#04-modern-cli-with-click-framework)
- [Argument Types and Patterns](#argument-types-and-patterns)
  - [argparse Argument Types](#argparse-argument-types)
    - [Basic Argument Types](#basic-argument-types)
    - [Advanced Argument Features](#advanced-argument-features)
  - [docopt Patterns](#docopt-patterns)
    - [Usage Patterns](#usage-patterns)
    - [Pattern Elements](#pattern-elements)
- [Comprehensive CLI Examples](#comprehensive-cli-examples)
  - [File Processing Tool (argparse)](#file-processing-tool-argparse)
  - [Database CLI Tool (docopt)](#database-cli-tool-docopt)
- [How to Run Examples](#how-to-run-examples)
  - [Basic argparse Example](#basic-argparse-example)
  - [docopt Example](#docopt-example)
  - [Packaged CLI Tool Example](#packaged-cli-tool-example)
  - [Modern CLI with Click Framework Example](#modern-cli-with-click-framework-example)
- [Advanced CLI Patterns](#advanced-cli-patterns)
  - [Subcommands with argparse](#subcommands-with-argparse)
  - [Configuration File Integration](#configuration-file-integration)
  - [Environment Variable Integration](#environment-variable-integration)
- [Best Practices](#best-practices)
  - [1. **Provide Clear Help Messages**](#1-provide-clear-help-messages)
  - [2. **Use Appropriate Argument Types**](#2-use-appropriate-argument-types)
  - [3. **Handle Errors Gracefully**](#3-handle-errors-gracefully)
  - [4. **Use Argument Groups for Organization**](#4-use-argument-groups-for-organization)
  - [5. **Provide Examples and Epilog**](#5-provide-examples-and-epilog)
- [Library Comparison](#library-comparison)
  - [Framework Comparison](#framework-comparison)
  - [When to Use Each](#when-to-use-each)
    - [Choose argparse when:](#choose-argparse-when)
    - [Choose docopt when:](#choose-docopt-when)
    - [Choose Click when:](#choose-click-when)
- [Common CLI Patterns](#common-cli-patterns)
  - [Progress Indicators](#progress-indicators)
  - [Logging Integration](#logging-integration)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Master Python's built-in argparse module
- Learn docopt for declarative argument parsing
- Explore modern CLI development with Click framework
- Create distributable CLI tools with entry points
- Understand different types of command-line arguments
- Create professional command-line interfaces with rich formatting
- Handle argument validation and error messages
- Build user-friendly help systems
- Design maintainable and installable CLI applications
- Package CLI tools for distribution
- Compare different CLI frameworks and choose the right tool

## Course Content

### 01. argparse - Built-in Argument Parsing
**File:** `01/main.py`

Learn comprehensive argument parsing with Python's built-in argparse module:

```python
#!/usr/bin/env python3

import argparse

def main():
    # Create a parser
    parser = argparse.ArgumentParser(
        description='A simple example to demonstrate how argparse works.'
    )

    # Add command-line arguments
    parser.add_argument('-f', '--file', type=str, help='Path to the input file.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
    parser.add_argument('-n', '--number', type=int, default=1, help='A number to process (default: 1).')
    # Positional argument (required, no '-' or '--' prefix)
    parser.add_argument('output', type=str, help='Name of the output file.')

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    if args.verbose:
        print('Verbose mode is ON.')
        print(f'Input file: {args.file}')
        print(f'Number: {args.number}')
        print(f'Output file: {args.output}')
    else:
        print(f'Processing {args.output}...')

if __name__ == '__main__':
    main()
```

**Key Concepts:**
- `ArgumentParser()` for creating command-line parsers
- Optional arguments with `-` and `--` prefixes
- Positional arguments (required by default)
- `action='store_true'` for boolean flags
- Type conversion with `type=int`, `type=str`
- Default values with `default=`
- Automatic help generation (`-h`, `--help`)

### 02. docopt - Declarative Argument Parsing
**Files:** `02/main.py`, `02/requirements.txt`

Learn elegant argument parsing using docopt's declarative approach:

**Requirements (`02/requirements.txt`)**
```pip-requirements
docopt-ng
```

**Application Code (`02/main.py`)**
```python
#!/usr/bin/env python3

'''
Usage:
    main.py [--file=<file>] [-v] [--number=<number>] <output>

A simple example to demonstrate how argparse works.

positional arguments:
  <output>                Name of the output file.

options:
  -h, --help            show this help message and exit
  -f, --file=<file>     Path to the input file.
  -v, --verbose         Enable verbose output.
  -n, --number=<number> A number to process [default: 1].
'''

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0')

    # Use the parsed arguments
    if args['--verbose']:
        print('Verbose mode is ON.')
        print(f'Input file: {args["--file"]}')
        print(f'Number: {args["--number"]}')
        print(f'Output file: {args["<output>"]}')
    else:
        print(f'Processing {args["<output>"]}...')
```

**Key Concepts:**
- Docstring-based argument specification
- Usage patterns in docstring
- Automatic parsing from docstring format
- Dictionary-based argument access
- Built-in version support
- Less boilerplate code than argparse

### 03. Packaged CLI Tool with Entry Points
**Files:** `03/src/animal/cli.py`, `03/pyproject.toml`, `03/examples/main.py`

Learn to create distributable CLI tools with entry points and professional packaging:

**CLI Module (`03/src/animal/cli.py`)**
```python
#!/usr/bin/env python3

'''
Usage:
    animal dog --name=<name> --kind=<kind>

options:
    -h, --help          Show this help message.
    --name=<name>       Name of the dog.
    --kind=<kind>       Kind/Breed of the dog.
'''

from docopt import docopt
from animal.mammalia import Dog

def main():
    args = docopt(__doc__, version='0.1.0')

    # Use the parsed arguments
    if args['dog']:
        dog = Dog(name=args['--name'], kind=args['--kind'])
        dog.hello()
        dog.run()
```

**Package Configuration (`03/pyproject.toml`)**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "animal"
description = "A simple animal package"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "docopt-ng>=0.9.0, <1"
]
dynamic = ["version"]

[project.scripts]
animal = "animal.cli:main"

[project.optional-dependencies]
dev = ["pytest"]

[tool.hatch.build.targets.wheel]
packages = ["src/animal"]

[tool.hatch.version]
path = "src/animal/__about__.py"

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
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
- CLI entry points in `[project.scripts]`
- Packaged CLI tools with dependencies
- Professional package structure
- Integration of CLI and library functionality
- Installation creates system-wide commands
- Version management and testing integration

### 04. Modern CLI with Click Framework
**Files:** `04/src/animal/cli.py`, `04/pyproject.toml`, `04/README.md`

Learn to create modern, user-friendly CLI applications using the Click framework with rich formatting:

**CLI Module (`04/src/animal/cli.py`)**
```python
#!/usr/bin/env python3

import rich_click as click
from animal.mammalia import Dog

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='Name of the dog.')
@click.option('--kind', required=True, help='Kind/Breed of the dog.')
def dog(name: str, kind: str):
    instance = Dog(name=name, kind=kind)
    instance.hello()
    instance.run()

if __name__ == '__main__':
    cli()
```

**Package Configuration (`04/pyproject.toml`)**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "animal"
description = "A simple animal package"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "click>=8.3.0, <9",
    "rich-click>=1.9.4, <2",
]
dynamic = ["version"]

[project.scripts]
animal = "animal.cli:cli"

[project.optional-dependencies]
dev = ["pytest"]

[tool.hatch.build.targets.sdist]
include = ["src/animal"]
```

**Key Concepts:**
- Click decorators for command definition (`@click.group()`, `@cli.command()`)
- Rich-click for enhanced formatting and styling
- Type hints for better code clarity
- Required options with `required=True`
- Modern dependency management with version constraints
- Group-based command organization
- Professional package metadata and classifiers

## Argument Types and Patterns

### argparse Argument Types

#### Basic Argument Types
```python
import argparse

parser = argparse.ArgumentParser()

# String argument (default)
parser.add_argument('--name', type=str)

# Integer argument
parser.add_argument('--count', type=int)

# Float argument
parser.add_argument('--rate', type=float)

# Boolean flag
parser.add_argument('--verbose', action='store_true')

# Store false flag
parser.add_argument('--quiet', action='store_false')

# Choice from list
parser.add_argument('--format', choices=['json', 'xml', 'csv'])
```

#### Advanced Argument Features
```python
# Multiple values
parser.add_argument('--files', nargs='+', help='One or more files')
parser.add_argument('--coords', nargs=2, type=float, help='X Y coordinates')
parser.add_argument('--optional-files', nargs='*', help='Zero or more files')

# Required optional arguments
parser.add_argument('--config', required=True, help='Configuration file')

# Argument groups
group = parser.add_argument_group('authentication')
group.add_argument('--username')
group.add_argument('--password')

# Mutually exclusive groups
group = parser.add_mutually_exclusive_group()
group.add_argument('--verbose', action='store_true')
group.add_argument('--quiet', action='store_true')
```

### docopt Patterns

#### Usage Patterns
```python
'''
Usage:
    program.py [-v | --verbose] [--output=<file>] <input>
    program.py --help
    program.py --version

Options:
    -v, --verbose     Verbose output
    --output=<file>   Output file [default: stdout]
    -h, --help        Show this help
    --version         Show version
'''
```

#### Pattern Elements
- `<argument>` - Positional arguments
- `--option` - Long options
- `-o` - Short options
- `[optional]` - Optional elements
- `(required)` - Required elements (rarely used)
- `element...` - Repeating elements
- `|` - Mutually exclusive elements

## Comprehensive CLI Examples

### File Processing Tool (argparse)
```python
#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

def process_file(input_file, output_file, verbose=False):
    if verbose:
        print(f"Processing {input_file} -> {output_file}")

    # Actual file processing logic here
    with open(input_file, 'r') as f:
        content = f.read()

    with open(output_file, 'w') as f:
        f.write(content.upper())  # Example transformation

def main():
    parser = argparse.ArgumentParser(
        description='Process text files',
        epilog='Example: %(prog)s input.txt -o output.txt --verbose'
    )

    parser.add_argument('input', type=Path, help='Input file path')
    parser.add_argument('-o', '--output', type=Path, required=True,
                       help='Output file path')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--encoding', default='utf-8',
                       help='File encoding (default: utf-8)')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()

    # Validate input file exists
    if not args.input.exists():
        parser.error(f"Input file '{args.input}' does not exist")

    # Create output directory if needed
    args.output.parent.mkdir(parents=True, exist_ok=True)

    try:
        process_file(args.input, args.output, args.verbose)
        if args.verbose:
            print("Processing completed successfully")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```

### Database CLI Tool (docopt)
```python
#!/usr/bin/env python3

'''Database Management Tool

Usage:
    dbctl create <database> [--type=<type>] [--verbose]
    dbctl delete <database> [--force] [--verbose]
    dbctl list [--format=<fmt>] [--verbose]
    dbctl backup <database> <destination> [--verbose]
    dbctl restore <database> <source> [--verbose]
    dbctl (-h | --help)
    dbctl --version

Arguments:
    <database>      Database name
    <destination>   Backup destination path
    <source>        Restore source path

Options:
    -h --help                Show this screen
    --version                Show version
    -v --verbose             Verbose output
    -f --force               Force operation without confirmation
    --type=<type>            Database type [default: sqlite]
    --format=<fmt>           Output format [default: table]

Examples:
    dbctl create mydb --type=postgresql --verbose
    dbctl backup mydb /backups/mydb.sql
    dbctl list --format=json
'''

from docopt import docopt
import sys

def create_database(name, db_type='sqlite', verbose=False):
    if verbose:
        print(f"Creating {db_type} database: {name}")
    # Database creation logic here

def delete_database(name, force=False, verbose=False):
    if not force:
        response = input(f"Delete database '{name}'? (y/N): ")
        if response.lower() != 'y':
            print("Operation cancelled")
            return

    if verbose:
        print(f"Deleting database: {name}")
    # Database deletion logic here

def list_databases(format_type='table', verbose=False):
    if verbose:
        print(f"Listing databases in {format_type} format")
    # Database listing logic here

def main():
    args = docopt(__doc__, version='Database CLI Tool 1.0')

    verbose = args['--verbose']

    try:
        if args['create']:
            create_database(args['<database>'], args['--type'], verbose)
        elif args['delete']:
            delete_database(args['<database>'], args['--force'], verbose)
        elif args['list']:
            list_databases(args['--format'], verbose)
        elif args['backup']:
            # Backup logic
            pass
        elif args['restore']:
            # Restore logic
            pass
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## How to Run Examples

### Basic argparse Example
```bash
# Navigate to corresponding directory
cd lesson-14/01

# Show help
python3 main.py --help

# Basic usage (positional argument required)
python3 main.py output.txt

# With optional arguments
python3 main.py -f input.txt -v -n 42 output.txt

# Long form options
python3 main.py --file input.txt --verbose --number 42 output.txt
```

### docopt Example
```bash
cd lesson-14/02

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Show help
python3 main.py --help

# Show version
python3 main.py --version

# Basic usage
python3 main.py output.txt

# With optional arguments
python3 main.py -f input.txt -v --number 42 output.txt
```

### Packaged CLI Tool Example
```bash
cd lesson-14/03

# Install requirements for development
python3 -m venv .venv
source .venv/bin/activate

# Install the package in development mode
pip install -e .[dev]

# Run the installed CLI command
animal dog --name="Maru" --kind="Shiba"

# Or run tests
pytest

# Or run the example script
python3 examples/main.py

# Build the package for distribution
python3 -m build

# The 'animal' command is now available system-wide after installation
```

### Modern CLI with Click Framework Example
```bash
cd lesson-14/04

# Install requirements for development
python3 -m venv .venv
source .venv/bin/activate

# Install the package in development mode
pip install -e .[dev]

# Run the installed CLI command with rich formatting
animal dog --name="Maru" --kind="Shiba"

# Or run tests
pytest

# The CLI will display enhanced help with rich formatting
animal dog --help

# Build the package for distribution
python3 -m build

# The 'animal' command is now available system-wide with rich formatting
```

## Advanced CLI Patterns

### Subcommands with argparse
```python
import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog='mytool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create subcommand
    create_parser = subparsers.add_parser('create', help='Create resource')
    create_parser.add_argument('name', help='Resource name')
    create_parser.add_argument('--type', default='default', help='Resource type')

    # Delete subcommand
    delete_parser = subparsers.add_parser('delete', help='Delete resource')
    delete_parser.add_argument('name', help='Resource name')
    delete_parser.add_argument('--force', action='store_true', help='Force deletion')

    # List subcommand
    list_parser = subparsers.add_parser('list', help='List resources')
    list_parser.add_argument('--format', choices=['table', 'json'], default='table')

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'create':
        print(f"Creating {args.type} resource: {args.name}")
    elif args.command == 'delete':
        print(f"Deleting resource: {args.name} (force: {args.force})")
    elif args.command == 'list':
        print(f"Listing resources in {args.format} format")
    else:
        parser.print_help()
```

### Configuration File Integration
```python
import argparse
import configparser
import json
from pathlib import Path

def load_config(config_file):
    """Load configuration from file"""
    config_path = Path(config_file)

    if not config_path.exists():
        return {}

    if config_path.suffix == '.json':
        with open(config_path) as f:
            return json.load(f)
    elif config_path.suffix in ['.ini', '.cfg']:
        config = configparser.ConfigParser()
        config.read(config_path)
        return dict(config['DEFAULT']) if 'DEFAULT' in config else {}

    return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=Path, help='Configuration file')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--output', help='Output file')

    args = parser.parse_args()

    # Load configuration
    config = {}
    if args.config:
        config = load_config(args.config)

    # Command line arguments override config file
    verbose = args.verbose or config.get('verbose', False)
    output = args.output or config.get('output', 'default.txt')

    print(f"Verbose: {verbose}, Output: {output}")
```

### Environment Variable Integration
```python
import argparse
import os

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--api-key',
                       default=os.getenv('API_KEY'),
                       help='API key (or set API_KEY environment variable)')
    parser.add_argument('--database-url',
                       default=os.getenv('DATABASE_URL', 'sqlite:///default.db'),
                       help='Database URL')
    parser.add_argument('--debug',
                       action='store_true',
                       default=os.getenv('DEBUG', '').lower() in ['1', 'true', 'yes'],
                       help='Enable debug mode')

    args = parser.parse_args()

    if not args.api_key:
        parser.error("API key is required (use --api-key or set API_KEY environment variable)")

    print(f"API Key: {args.api_key[:8]}...")
    print(f"Database: {args.database_url}")
    print(f"Debug: {args.debug}")
```

## Best Practices

### 1. **Provide Clear Help Messages**
```python
# Good: Descriptive help messages
parser.add_argument('--timeout', type=int, default=30,
                   help='Request timeout in seconds (default: 30)')

# Avoid: Unclear or missing help
parser.add_argument('--timeout', type=int, default=30)
```

### 2. **Use Appropriate Argument Types**
```python
# Good: Use pathlib.Path for file paths
parser.add_argument('--input', type=Path, help='Input file')

# Good: Use custom types for validation
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Must be positive integer")
    return ivalue

parser.add_argument('--count', type=positive_int)
```

### 3. **Handle Errors Gracefully**
```python
def main():
    parser = argparse.ArgumentParser()
    # ... add arguments ...

    try:
        args = parser.parse_args()

        # Validate arguments
        if args.input and not Path(args.input).exists():
            parser.error(f"Input file '{args.input}' does not exist")

        # Run main logic
        process(args)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```

### 4. **Use Argument Groups for Organization**
```python
parser = argparse.ArgumentParser()

# Input/Output group
io_group = parser.add_argument_group('input/output options')
io_group.add_argument('--input', help='Input file')
io_group.add_argument('--output', help='Output file')

# Processing group
proc_group = parser.add_argument_group('processing options')
proc_group.add_argument('--threads', type=int, help='Number of threads')
proc_group.add_argument('--memory', help='Memory limit')
```

### 5. **Provide Examples and Epilog**
```python
parser = argparse.ArgumentParser(
    description='Process data files',
    epilog='''
Examples:
  %(prog)s input.txt --output result.txt --verbose
  %(prog)s *.csv --format json --threads 4
  %(prog)s --config settings.ini input.txt
    ''',
    formatter_class=argparse.RawDescriptionHelpFormatter
)
```

## Library Comparison

### Framework Comparison

| Feature | argparse | docopt | Click |
|---------|----------|--------|-------|
| **Learning Curve** | Moderate | Easy | Easy |
| **Code Verbosity** | Verbose | Concise | Moderate |
| **Flexibility** | High | Medium | High |
| **Validation** | Built-in | Manual | Built-in |
| **Help Generation** | Automatic | From docstring | Automatic + Rich |
| **Subcommands** | Native support | Manual parsing | Native + Groups |
| **Dependencies** | Built-in | Third-party | Third-party |
| **Performance** | Fast | Slower | Fast |
| **Type Hints** | Manual | None | Native support |
| **Rich Formatting** | Basic | Basic | Advanced |
| **Testing Support** | Manual | Manual | Built-in |
| **Plugin System** | None | None | Extensive |

### When to Use Each

#### Choose argparse when:
- Building complex CLI applications
- Need extensive validation and error handling
- Want to minimize dependencies (built-in)
- Require maximum flexibility and control
- Working with legacy Python code

#### Choose docopt when:
- Building simple to medium CLI tools
- Want readable and maintainable code
- Prefer declarative over imperative
- Documentation-driven development approach
- Rapid prototyping

#### Choose Click when:
- Building modern, user-friendly CLI applications
- Want rich formatting and beautiful help pages
- Need extensive testing capabilities
- Require plugin systems and extensibility
- Working with complex command hierarchies
- Want type hint integration
- Building distributable CLI packages

## Common CLI Patterns

### Progress Indicators
```python
import argparse
from tqdm import tqdm
import time

def process_items(items, verbose=False):
    if verbose:
        items = tqdm(items, desc="Processing")

    for item in items:
        # Simulate processing
        time.sleep(0.1)
        if verbose:
            items.set_postfix(current=item)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--count', type=int, default=10)

    args = parser.parse_args()

    items = range(args.count)
    process_items(items, args.verbose)
```

### Logging Integration
```python
import argparse
import logging

def setup_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--log-file', help='Log file path')

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.verbose)
    if args.log_file:
        file_handler = logging.FileHandler(args.log_file)
        logging.getLogger().addHandler(file_handler)

    logging.info("Application started")
    # Application logic here
```

## Practice Suggestions

1. **CLI Calculator**: Build a calculator with different operations as subcommands
2. **File Manager**: Create a CLI tool for file operations (copy, move, delete)
3. **Log Analyzer**: Build a tool to analyze log files with various filters
4. **Configuration Manager**: Create a tool to manage application configurations
5. **API Client**: Build a CLI client for REST APIs with different endpoints
6. **Backup Tool**: Create a backup utility with various options and strategies

## Common Pitfalls

- **Missing Help Messages**: Always provide clear help for arguments
- **Poor Error Handling**: Handle invalid inputs gracefully
- **Inconsistent Naming**: Use consistent naming for similar options across tools
- **No Examples**: Provide usage examples in help or documentation
- **Overcomplicating**: Keep CLI simple and intuitive
- **Ignoring Standards**: Follow POSIX conventions for command-line interfaces

## Related Resources

- [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [docopt Documentation](http://docopt.org/)
- [Click Documentation](https://click.palletsprojects.com/) - Modern CLI framework with rich features
- [Rich-Click](https://github.com/ewels/rich-click) - Enhanced Click with rich formatting
- [Typer](https://typer.tiangolo.com/) - Modern CLI framework based on type hints
- [GNU/POSIX CLI Standards](https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html)
- [Command Line Interface Guidelines](https://clig.dev/)
- [Click Examples and Patterns](https://click.palletsprojects.com/en/8.1.x/complex/)