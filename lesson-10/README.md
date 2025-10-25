# Lesson 10 - Python Logging  <!-- omit in toc -->

This lesson covers Python's logging system, from basic console logging to advanced configuration-based logging with file rotation and multiple handlers.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Basic Logging](#01-basic-logging)
  - [02. Advanced Configuration-Based Logging](#02-advanced-configuration-based-logging)
- [Logging Components](#logging-components)
  - [Log Levels (in order of severity)](#log-levels-in-order-of-severity)
  - [Handlers](#handlers)
  - [Formatters](#formatters)
- [Logging Configuration Patterns](#logging-configuration-patterns)
  - [Basic Console Logging](#basic-console-logging)
  - [File Logging with Rotation](#file-logging-with-rotation)
  - [Multi-Handler Setup](#multi-handler-setup)
- [How to Run](#how-to-run)
- [Best Practices](#best-practices)
  - [1. **Use Appropriate Log Levels**](#1-use-appropriate-log-levels)
  - [2. **Use Logger Hierarchy**](#2-use-logger-hierarchy)
  - [3. **Lazy String Formatting**](#3-lazy-string-formatting)
  - [4. **Structured Configuration**](#4-structured-configuration)
  - [5. **Exception Logging**](#5-exception-logging)
- [Advanced Topics](#advanced-topics)
  - [Time-Based Log Rotation](#time-based-log-rotation)
  - [Custom Formatter](#custom-formatter)
  - [Context Managers for Logging](#context-managers-for-logging)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand Python's logging system
- Master basic logging configuration
- Learn logging levels and their use cases
- Understand advanced logging with configuration files
- Learn about file handlers and log rotation
- Master logger hierarchy and multiple handlers
- Understand logging best practices

## Course Content

### 01. Basic Logging
**File:** `01/main.py`

Learn the fundamentals of Python logging with basic configuration:

```python
#!/usr/bin/env python3

#############################
# Logging
#############################
import logging
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z',
    level=logging.INFO
)

#############################
# Main
#############################
if __name__ == '__main__':
    logging.debug('debug')      # This will not be shown due to log level
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')

    try:
        1 / 0
    except Exception as err:
        logging.exception(err)  # Automatically includes stack trace
```

**Key Concepts:**
- `logging.basicConfig()` for simple logging setup
- Log format with timestamp and level
- Five logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- `logging.exception()` for exception logging with stack traces
- Log level filtering (DEBUG messages not shown when level is INFO)
- ISO 8601 datetime formatting

### 02. Advanced Configuration-Based Logging
**Files:** `02/logging.conf`, `02/main.py`, `02/requirements.txt`

Learn advanced logging with YAML configuration files:

**Requirements (`02/requirements.txt`)**
```pip-requirements
pyyaml
```

**Logging Configuration (`02/logging.conf`)**
```yaml
version: 1

handlers:
  console:
    class: logging.StreamHandler
    formatter: tag
    level: INFO
    stream: ext://sys.stdout
  myfile:
    class: logging.handlers.RotatingFileHandler
    formatter: timestamp
    level: DEBUG
    filename: out.log
    backupCount: 3
    maxBytes: 1048576

formatters:
  tag:
    format: '[%(levelname)s] %(message)s'
  timestamp:
    format: '%(asctime)s [%(levelname)s] %(message)s'
    datefmt: '%Y-%m-%dT%H:%M:%S'

loggers:
  demo:
    handlers: [console, myfile]
    level: DEBUG
```

**Application Code (`02/main.py`)**
```python
#!/usr/bin/env python3

#############################
# Logging
#############################
import logging
from logging import config
from pathlib import Path
import yaml

workdir = Path(__file__).parent
with open(workdir / 'logging.conf') as f:
    conf = yaml.safe_load(f)
    config.dictConfig(conf)
log = logging.getLogger('demo')

#############################
# Main
#############################
if __name__ == '__main__':
    log.debug('debug')      # Will be shown in file but not console
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
```

**Key Concepts:**
- `logging.config.dictConfig()` for configuration-based setup
- Multiple handlers: console and rotating file
- Different formatters for different outputs
- `RotatingFileHandler` with automatic log rotation
- Logger hierarchy with named loggers
- Handler-specific log levels
- External stream references (`ext://sys.stdout`)

## Logging Components

### Log Levels (in order of severity)
1. **DEBUG**: Detailed diagnostic information
2. **INFO**: General information about program execution
3. **WARNING**: Something unexpected but not an error
4. **ERROR**: Error occurred but program continues
5. **CRITICAL**: Serious error, program may not continue

### Handlers
- **StreamHandler**: Output to console/streams
- **FileHandler**: Output to files
- **RotatingFileHandler**: File output with automatic rotation
- **TimedRotatingFileHandler**: Time-based log rotation
- **SMTPHandler**: Email notifications for critical errors

### Formatters
Common format specifiers:
- `%(asctime)s`: Timestamp
- `%(levelname)s`: Log level name
- `%(message)s`: Log message
- `%(name)s`: Logger name
- `%(filename)s`: Source filename
- `%(lineno)d`: Line number
- `%(funcName)s`: Function name

## Logging Configuration Patterns

### Basic Console Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('Application started')
```

### File Logging with Rotation
```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create rotating file handler
handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)
handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

logger.addHandler(handler)
```

### Multi-Handler Setup
```python
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console handler (INFO and above)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('[%(levelname)s] %(message)s')
console_handler.setFormatter(console_format)

# File handler (DEBUG and above)
file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-10/01
python3 main.py
```

```bash
cd lesson-10/02
pip install -r requirements.txt
python3 main.py
```

**Note:** The second example will create an `out.log` file with detailed logging information.

## Best Practices

### 1. **Use Appropriate Log Levels**
```python
# Good: Use appropriate levels
logger.debug('Detailed diagnostic info')      # Development
logger.info('Normal program flow')            # Production info
logger.warning('Unexpected but handled')      # Potential issues
logger.error('Error occurred')                # Errors
logger.critical('System failure')             # Critical failures

# Avoid: Using wrong levels
logger.error('User logged in')  # Should be INFO
logger.info('Database connection failed')  # Should be ERROR
```

### 2. **Use Logger Hierarchy**
```python
# Good: Use module-specific loggers
logger = logging.getLogger(__name__)

# Good: Create child loggers
db_logger = logging.getLogger('myapp.database')
api_logger = logging.getLogger('myapp.api')

# Avoid: Using root logger everywhere
logging.info('This uses root logger')  # Less flexible
```

### 3. **Lazy String Formatting**
```python
# Good: Let logging handle formatting
logger.info('User %s logged in with ID %d', username, user_id)

# Avoid: Pre-formatting strings
logger.info(f'User {username} logged in with ID {user_id}')  # Always evaluated
```

### 4. **Structured Configuration**
```python
# Good: Use configuration files for complex setups
with open('logging.conf') as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

# Good: Separate configuration from code
# Avoid: Hard-coding complex logging setup in application code
```

### 5. **Exception Logging**
```python
# Good: Use exception() for exception logging
try:
    risky_operation()
except Exception as e:
    logger.exception('Operation failed')  # Includes stack trace

# Good: Log and re-raise
try:
    critical_operation()
except Exception as e:
    logger.error('Critical operation failed: %s', e)
    raise  # Re-raise the exception

# Avoid: Swallowing exceptions
try:
    operation()
except Exception:
    pass  # Silent failure is bad
```

## Advanced Topics

### Time-Based Log Rotation
```python
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',  # Rotate at midnight
    interval=1,       # Every 1 day
    backupCount=30    # Keep 30 days of logs
)
```

### Custom Formatter
```python
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
        'RESET': '\033[0m'      # Reset
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        record.levelname = f"{log_color}{record.levelname}{self.COLORS['RESET']}"
        return super().format(record)
```

### Context Managers for Logging
```python
import logging
from contextlib import contextmanager

@contextmanager
def log_context(operation_name):
    logger = logging.getLogger(__name__)
    logger.info(f'Starting {operation_name}')
    start_time = time.time()
    try:
        yield
        logger.info(f'Completed {operation_name} in {time.time() - start_time:.2f}s')
    except Exception as e:
        logger.error(f'Failed {operation_name}: {e}')
        raise

# Usage
with log_context('database backup'):
    perform_backup()
```

## Practice Suggestions

1. **Log Level Experimentation**: Create applications with different log levels and observe the output
2. **Multi-Handler Setup**: Configure logging to write to console, file, and potentially email
3. **Structured Logging**: Implement JSON-formatted logs for better parsing
4. **Performance Monitoring**: Add logging to measure function execution times
5. **Error Tracking**: Implement comprehensive error logging with context information
6. **Log Analysis**: Write scripts to analyze and visualize log files

## Common Pitfalls

- **Over-logging**: Too many DEBUG messages in production
- **Under-logging**: Not enough context for debugging issues
- **Blocking handlers**: Synchronous logging in high-performance applications
- **Security issues**: Logging sensitive information (passwords, tokens)
- **Resource leaks**: Not properly closing file handlers
- **Format inconsistency**: Different log formats across modules

## Related Resources

- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Logging Configuration](https://docs.python.org/3/library/logging.config.html)
- [Logging Handlers](https://docs.python.org/3/library/logging.handlers.html)
- [Logging Best Practices](https://docs.python.org/3/howto/logging.html)
- [Structured Logging](https://structlog.readthedocs.io/)