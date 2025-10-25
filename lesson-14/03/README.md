# Get Startted

This lesson guides you through setting up and running the command-line interface (CLI) application for the `animal` package, which includes a `dog` command that allows users to create and interact with dog objects.

```bash
# Install pytest if you haven't already
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Run the tests
pytest

# Run the CLI application
animal dog --name=Maru --kind=Shiba
```
