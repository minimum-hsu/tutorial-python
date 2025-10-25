# Lesson 09 - Python Data Format Parsing

This lesson covers parsing various data formats commonly used in software development, including configuration files, structured data formats, and markup languages.

## Learning Objectives

- Master INI configuration file parsing
- Learn JSON data processing
- Understand HTML parsing techniques
- Master XML parsing with different approaches
- Learn CSV data processing
- Understand YAML configuration handling
- Master TOML format parsing
- Compare different parsing approaches and use cases

## Course Content

### 01. INI Configuration Files
**Files:** `01/config.ini`, `01/ini_parser.py`

Learn to parse INI configuration files using Python's built-in configparser:

**INI Parser (`01/ini_parser.py`)**
```python
#!/usr/bin/env python3

from configparser import ConfigParser
from pathlib import Path

workdir = Path(__file__).parent
config = ConfigParser()
config.read(workdir / 'config.ini')

for section in config.sections():
    for key in config[section]:
        print('section: {}, key: {}, value: {}'.format(
            section, key, config[section][key]))
```

**Key Concepts:**
- `ConfigParser` for reading INI files
- Section-based configuration structure
- Accessing sections and keys
- Common use case for application configuration
- Built-in Python standard library support

### 02. JSON Data Processing
**Files:** `02/config.json`, `02/json_parser.py`

Learn to parse JSON data format for structured data exchange:

**JSON Parser (`02/json_parser.py`)**
```python
#!/usr/bin/env python3

from json import load
from pathlib import Path

workdir = Path(__file__).parent
with open(workdir / 'config.json', 'r') as myfile:
    config = load(myfile)
    print(config)

    for index, account in enumerate(config['account']):
        print('account', index)
        for key, value in account.items():
            print('{}: {}'.format(key, value))
```

**Key Concepts:**
- `json.load()` for reading JSON files
- JSON to Python dict conversion
- Nested data structure handling
- Array iteration with `enumerate()`
- Wide compatibility and human-readable format

### 03. HTML Parsing
**Files:** `03/rate.html`, `03/html_parser.py`, `03/html_parser_v2.py`

Learn different approaches to parse HTML content:

**Basic HTML Parser (`03/html_parser.py`)**
```python
#!/usr/bin/env python3

from html.parser import HTMLParser
from html.entities import name2codepoint
from pathlib import Path

class MyHTMLParser(HTMLParser):
    __in_tbody = False
    __in_td_th = False
    __in_tr = False
    __print = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tbody':
            self.__in_tbody = True
        elif tag == 'tr':
            self.__in_tr = True
        elif tag in ('td', 'th'):
            self.__in_td_th = True

        for attr in attrs:
            if attr[1] and 'print_hide' in attr[1]:
                self.__print = True

    def handle_endtag(self, tag):
        self.__print = False
        if tag == 'tbody':
            self.__in_tbody = False
        elif tag == 'tr':
            self.__in_tr = False
            if self.__in_tbody:
                print('')
        elif tag in ('td', 'th'):
            self.__in_td_th = False

    def handle_data(self, data):
        if self.__in_tbody and self.__in_td_th:
            data = data.strip()
            if self.__print and data and data not in ('查詢'):
                print(data, end=',')

if __name__ == '__main__':
    workdir = Path(__file__).parent
    myfile = workdir / 'rate.html'
    content = myfile.read_text()

    parser = MyHTMLParser()
    parser.feed(content)
```

**Path-Based HTML Parser (`03/html_parser_v2.py`)**
```python
#!/usr/bin/env python3

from html.parser import HTMLParser
from pathlib import Path

class MyHTMLParser(HTMLParser):
    candidate = [
        '.tbody.tr.td',
        '.tbody.tr.td.div.div'
    ]
    __current_path = ''
    __print = False

    def handle_starttag(self, tag, attrs):
        self.__current_path += '.' + tag
        for attr in attrs:
            if attr[1] and 'print_hide' in attr[1]:
                self.__print = True

    def handle_endtag(self, tag):
        self.__print = False
        if self.__current_path.endswith('.tbody.tr'):
            print('')
        self.__current_path = self.__current_path[:-len(tag)-1]

    def handle_data(self, data):
        for template in self.candidate:
            if self.__current_path.endswith(template):
                data = data.strip()
                if self.__print and data and data not in ('查詢'):
                    print(data, end=',')
```

**Key Concepts:**
- `HTMLParser` class for custom HTML parsing
- State tracking with boolean flags
- Path-based element tracking
- Attribute filtering and data extraction
- Custom parsing logic for specific HTML structures

### 04. XML Parsing
**Files:** `04/news.xml`, `04/xml_parser_et.py`, `04/xml_parser_dom.py`, `04/xml_parser_sax.py`

Learn three different approaches to XML parsing:

**ElementTree Approach (`04/xml_parser_et.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path
import xml.etree.ElementTree as ET

def parse_appledaily_news(file_: str):
    tree = ET.parse(file_)
    root = tree.getroot()

    news = [(item.find('title').text, item.find('link').text)
            for item in root.iter('item')]
    return news

if __name__ == '__main__':
    workdir = Path(__file__).parent
    news = parse_appledaily_news(workdir / 'news.xml')
    print(*news, sep='\n')
```

**DOM Approach (`04/xml_parser_dom.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path
from xml.dom.minidom import parse

def parse_appledaily_news(file_: str):
    dom = parse(file_)
    root = dom.documentElement
    items = [x for x in root.getElementsByTagName('channel')[0].childNodes
             if x.nodeType is root.ELEMENT_NODE and x.nodeName == 'item']

    def parse_item(item):
        for node in item.childNodes:
            if node.nodeName == 'title':
                title = parse_data(node)
            elif node.nodeName == 'link':
                link = parse_data(node)
        return title, link

    def parse_data(node) -> str:
        for n in node.childNodes:
            if n.nodeType in (root.TEXT_NODE, root.CDATA_SECTION_NODE):
                return n.data

    news = [parse_item(item) for item in items]
    return news
```

**SAX Approach (`04/xml_parser_sax.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path
from xml.sax import parse, ContentHandler

class AppleDailyNewsHandler(ContentHandler):
    __title = ''
    __link = ''
    __current_path = ''

    def startElement(self, tag, attrs):
        self.__current_path += '.' + tag

    def endElement(self, tag):
        if tag == 'item':
            print((self.__title, self.__link))
        self.__current_path = self.__current_path[:-len(tag)-1]

    def characters(self, data):
        if self.__current_path.endswith('.item.title'):
            self.__title = data
        elif self.__current_path.endswith('.item.link'):
            self.__link = data

if __name__ == '__main__':
    workdir = Path(__file__).parent
    parse(workdir / 'news.xml', AppleDailyNewsHandler())
```

**Key Concepts:**
- **ElementTree**: Tree-based, memory-efficient, Pythonic
- **DOM**: Full document model, memory-intensive, W3C standard
- **SAX**: Event-driven, memory-efficient, streaming
- Different use cases for each approach
- CDATA section handling

### 05. CSV Data Processing
**Files:** `05/weather.csv`, `05/csv_parser.py`

Learn to parse CSV files for tabular data:

**CSV Parser (`05/csv_parser.py`)**
```python
#!/usr/bin/env python3

from csv import DictReader
from pathlib import Path

def parse_weather(file_: str):
    with open(file_, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            print(row['SiteName'], row['Temperature'], row['Weather'])

if __name__ == '__main__':
    workdir = Path(__file__).parent
    parse_weather(workdir / 'weather.csv')
```

**Key Concepts:**
- `csv.DictReader` for dictionary-based CSV reading
- Automatic header detection
- Column access by name
- Simple tabular data processing
- Built-in CSV format handling

### 06. YAML Configuration
**Files:** `06/docker-compose.yml`, `06/requirements.txt`, `06/yaml_parser.py`

Learn to parse YAML files for configuration:

**Requirements (`06/requirements.txt`)**
```pip-requirements
pyyaml
```

**YAML Parser (`06/yaml_parser.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path
import yaml

def parser_yaml(file_: str) -> dict:
    with open(file_, 'r') as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    workdir = Path(__file__).parent
    data = parser_yaml(workdir / 'docker-compose.yml')
    print(data)
```

**Key Concepts:**
- `yaml.safe_load()` for secure YAML parsing
- Human-readable configuration format
- Support for complex nested structures
- External dependency management
- Common in DevOps and configuration management

### 07. TOML Configuration
**Files:** `07/pyproject.toml`, `07/toml_parser.py`

Learn to parse TOML files (Python 3.11+ built-in):

**TOML Parser (`07/toml_parser.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path
import tomllib

def parser_toml(file_: str) -> dict:
    with open(file_, 'rb') as f:  # Binary mode required
        return tomllib.load(f)

if __name__ == '__main__':
    workdir = Path(__file__).parent
    data = parser_toml(workdir / 'pyproject.toml')
    print(data)
```

**Key Concepts:**
- `tomllib` built-in module (Python 3.11+)
- Binary file mode requirement
- Popular in Python packaging (`pyproject.toml`)
- Clear, minimal configuration syntax
- Strong typing support

## Format Comparison

| Format | Use Case | Pros | Cons | Python Support |
|--------|----------|------|------|----------------|
| **INI** | Simple config | Easy to read/write | Limited nesting | Built-in |
| **JSON** | Data exchange | Universal, lightweight | No comments | Built-in |
| **XML** | Structured docs | Rich metadata | Verbose | Built-in |
| **CSV** | Tabular data | Simple, Excel compatible | Flat structure only | Built-in |
| **YAML** | Configuration | Human-readable | Indentation sensitive | External |
| **TOML** | Config files | Clear syntax | Less common | Built-in (3.11+) |

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-09/01
python3 ini_parser.py
```

```bash
cd lesson-0902
python3 json_parser.py
```

```bash
cd lesson-09/03
python3 html_parser.py
python3 html_parser_v2.py
```

```bash
cd lesson-09/04
python3 xml_parser_et.py
python3 xml_parser_dom.py
python3 xml_parser_sax.py
```

```bash
cd lesson-09/05
python3 csv_parser.py
```

```bash
cd lesson-09/06
pip install -r requirements.txt
python3 yaml_parser.py
```

```bash
cd lesson-09/07
python3 toml_parser.py
```

## Best Practices

### 1. **Choose the Right Parser**
```python
# For configuration files
config = ConfigParser()  # INI files
config = yaml.safe_load(f)  # YAML files
config = tomllib.load(f)  # TOML files

# For data exchange
data = json.load(f)  # JSON data

# For tabular data
reader = csv.DictReader(f)  # CSV files
```

### 2. **Handle Encoding Properly**
```python
# Specify encoding for text files
with open('file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# TOML requires binary mode
with open('file.toml', 'rb') as f:
    data = tomllib.load(f)
```

### 3. **Error Handling**
```python
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Configuration file not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

### 4. **Security Considerations**
```python
# Use safe_load for YAML to prevent code execution
data = yaml.safe_load(f)  # Good
# data = yaml.load(f)  # Dangerous!

# Validate data after parsing
if 'required_field' not in config:
    raise ValueError("Missing required configuration")
```

## Practice Suggestions

1. **Format Conversion**: Write tools to convert between different formats (JSON ↔ YAML ↔ TOML)
2. **Configuration Management**: Build a configuration loader that supports multiple formats
3. **Data Processing**: Parse real-world datasets (APIs, logs, exports)
4. **Web Scraping**: Practice HTML parsing with different websites
5. **Performance Testing**: Compare parsing performance for large files
6. **Validation**: Add schema validation for parsed data

## Advanced Topics

- **Schema Validation**: JSON Schema, YAML Schema validation
- **Stream Processing**: Handle large files without loading into memory
- **Custom Parsers**: Build domain-specific parsers
- **Performance Optimization**: Choose parsers based on file size and requirements
- **Security**: Sanitize and validate parsed data

## Related Resources

- [ConfigParser Documentation](https://docs.python.org/3/library/configparser.html)
- [JSON Documentation](https://docs.python.org/3/library/json.html)
- [HTML Parser Documentation](https://docs.python.org/3/library/html.parser.html)
- [XML Processing Documentation](https://docs.python.org/3/library/xml.html)
- [CSV Documentation](https://docs.python.org/3/library/csv.html)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [TOML Documentation](https://docs.python.org/3/library/tomllib.html)