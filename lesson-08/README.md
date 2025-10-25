# Lesson 08 - Python File I/O Operations

This lesson covers file input/output operations in Python, including reading files, writing files, and working with temporary files for safe file operations.

## Learning Objectives

- Master different file reading techniques
- Learn file writing methods
- Understand context managers for file operations
- Learn to work with temporary files and directories
- Understand file path handling with pathlib
- Master safe file operations and cleanup

## Course Content

### 01. File Reading Operations
**Files:** `01/reader_all.py`, `01/reader_line_by_line.py`, `01/reader_lines.py`, `01/fruit.txt`

Learn different approaches to reading file content:

**Read Entire File (`01/reader_all.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path

workdir = Path(__file__).parent
file = workdir / 'fruit.txt'
content = file.read_text()
print(content)
```

**Read Line by Line (`01/reader_line_by_line.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path

workdir = Path(__file__).parent

with open(workdir / 'fruit.txt', 'r') as myfile:
    while True:
        line = myfile.readline()
        if not line:  # End of file
            break
        print(line, end='')
```

**Read All Lines at Once (`01/reader_lines.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path

workdir = Path(__file__).parent

with open(workdir / 'fruit.txt', 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        print(line, end='')
```

**Key Concepts:**
- `pathlib.Path` for cross-platform path handling
- `Path(__file__).parent` to get script directory
- `file.read_text()` for simple file reading
- `with` statement for context management
- `readline()` for single line reading
- `readlines()` for reading all lines into a list
- Automatic file closure with context managers

### 02. File Writing Operations
**Files:** `02/writer.py`, `02/file_directed_output.py`

Learn different methods for writing data to files:

**Manual File Writing (`02/writer.py`)**
```python
#!/usr/bin/env python3

names = ['Alice', 'Bob', 'Charlie']

with open('/tmp/names.txt', 'w') as myfile:
    for user in names:
        myfile.write(user + '\n')  # Manual newline addition
```

**Print to File (`02/file_directed_output.py`)**
```python
#!/usr/bin/env python3

names = ['Alice', 'Bob', 'Charlie']

with open('/tmp/names.txt', 'w') as myfile:
    for user in names:
        print(user, file=myfile)  # Automatic newline
```

**Key Concepts:**
- `'w'` mode for writing (overwrites existing content)
- `myfile.write()` for manual string writing
- `print(data, file=myfile)` for formatted output to files
- Automatic newline handling with `print()`
- Context managers ensure proper file closure
- File path considerations (`/tmp/` on Unix systems)

### 03. Temporary File Operations
**Files:** `03/temp.py`, `03/tempfile_directed_output.py`

Learn to work with temporary files and directories safely:

**Basic Temporary Files (`03/temp.py`)**
```python
#!/usr/bin/env python3

import os
from tempfile import mkdtemp
from tempfile import mkstemp

def tempfile_demo():
    _, temp_path = mkstemp()  # Returns file descriptor and path
    print('temp file is', temp_path)

    with open(temp_path, 'w') as myfile:
        myfile.write('hello')

    os.remove(temp_path)  # Manual cleanup required

def tempfolder_demo():
    temp_path = mkdtemp()  # Create temporary directory
    print('temp folder is', temp_path)

    os.rmdir(temp_path)  # Manual cleanup required

if __name__ == '__main__':
    tempfile_demo()
    tempfolder_demo()
```

**Advanced Temporary Files (`03/tempfile_directed_output.py`)**
```python
#!/usr/bin/env python3

from tempfile import TemporaryDirectory
from tempfile import TemporaryFile

def tempfile_demo():
    myfile = TemporaryFile(mode='w+')  # Read/write mode
    print('hello', file=myfile)
    myfile.seek(0)  # Return to beginning
    print(myfile.readline(), end='')
    myfile.close()  # Automatic cleanup
    print('file is removed after closed')

def tempfolder_demo():
    with TemporaryDirectory() as myfolder:
        print('temp folder is', myfolder)
        # Use myfolder for temporary operations
    print('folder is removed after closed')  # Automatic cleanup

if __name__ == '__main__':
    tempfile_demo()
    tempfolder_demo()
```

**Key Concepts:**
- `mkstemp()` creates temporary file with manual cleanup
- `mkdtemp()` creates temporary directory with manual cleanup
- `TemporaryFile()` with automatic cleanup
- `TemporaryDirectory()` with context manager support
- `seek(0)` to reposition file pointer
- `'w+'` mode for read/write operations
- Automatic cleanup vs manual cleanup considerations

## File Operation Patterns

### Safe File Reading Pattern
```python
from pathlib import Path

def safe_read_file(filepath: Path) -> str:
    try:
        if filepath.exists() and filepath.is_file():
            return filepath.read_text(encoding='utf-8')
        else:
            raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
```

### Append to File Pattern
```python
def append_to_file(filepath: str, content: str):
    with open(filepath, 'a') as f:  # 'a' for append mode
        f.write(content + '\n')
```

### Binary File Operations
```python
def read_binary_file(filepath: str) -> bytes:
    with open(filepath, 'rb') as f:  # 'rb' for binary read
        return f.read()

def write_binary_file(filepath: str, data: bytes):
    with open(filepath, 'wb') as f:  # 'wb' for binary write
        f.write(data)
```

### File Processing with Error Handling
```python
def process_file_safely(filepath: str):
    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    # Process each line
                    processed = line.strip().upper()
                    print(f"Line {line_num}: {processed}")
                except Exception as e:
                    print(f"Error processing line {line_num}: {e}")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except PermissionError:
        print(f"Permission denied: {filepath}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

## File Mode Reference

| Mode | Description | Creates | Truncates | Position |
|------|-------------|---------|-----------|-----------|
| `'r'` | Read only | No | No | Beginning |
| `'w'` | Write only | Yes | Yes | Beginning |
| `'a'` | Append only | Yes | No | End |
| `'r+'` | Read/Write | No | No | Beginning |
| `'w+'` | Read/Write | Yes | Yes | Beginning |
| `'a+'` | Read/Append | Yes | No | End |

Add `'b'` for binary mode (e.g., `'rb'`, `'wb'`, `'ab'`)

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-08/01
python3 reader_all.py
python3 reader_line_by_line.py
python3 reader_lines.py
```

```bash
# Only for Unix/Linux/macOS
cd lesson-08/02
python3 writer.py
python3 file_directed_output.py
```

```bash
cd lesson-08/03
python3 temp.py
python3 tempfile_directed_output.py
```

## Best Practices

### 1. **Always Use Context Managers**
```python
# Good: Automatic file closure
with open('file.txt', 'r') as f:
    content = f.read()

# Avoid: Manual file handling
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget or skip on exceptions
```

### 2. **Handle Encoding Explicitly**
```python
# Good: Explicit encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Good: Using pathlib with encoding
from pathlib import Path
content = Path('file.txt').read_text(encoding='utf-8')
```

### 3. **Use pathlib for Path Operations**
```python
# Good: Cross-platform path handling
from pathlib import Path

data_dir = Path(__file__).parent / 'data'
file_path = data_dir / 'input.txt'

if file_path.exists():
    content = file_path.read_text()

# Avoid: String path manipulation
import os
data_dir = os.path.join(os.path.dirname(__file__), 'data')
file_path = os.path.join(data_dir, 'input.txt')
```

### 4. **Use Temporary Files for Safe Operations**
```python
# Good: Safe temporary operations
from tempfile import NamedTemporaryFile
import shutil

def safe_file_update(original_path, new_content):
    with NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write(new_content)
        tmp_path = tmp.name

    # Atomic operation
    shutil.move(tmp_path, original_path)
```

## Practice Suggestions

1. **File Processing**:
   - Create a program to count words in text files
   - Build a log file analyzer
   - Implement a simple file backup utility

2. **Data Format Handling**:
   - Read and write CSV files
   - Process JSON configuration files
   - Handle different text encodings

3. **Batch File Operations**:
   - Process multiple files in a directory
   - Implement file filtering and searching
   - Create file organization tools

4. **Temporary File Usage**:
   - Implement safe file editing operations
   - Create temporary data processing pipelines
   - Build caching systems with temporary storage

## Common Pitfalls

- **Not closing files**: Always use context managers
- **Encoding issues**: Specify encoding explicitly
- **Path separators**: Use pathlib for cross-platform compatibility
- **File permissions**: Handle permission errors gracefully
- **Memory usage**: Use line-by-line reading for large files
- **Temporary file cleanup**: Use proper temporary file APIs

## Related Resources

- [Python File Objects Documentation](https://docs.python.org/3/library/io.html)
- [pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [tempfile Module Documentation](https://docs.python.org/3/library/tempfile.html)
- [Context Managers Documentation](https://docs.python.org/3/library/contextlib.html)
- [File Handling Best Practices](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)