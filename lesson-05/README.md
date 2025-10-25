# Lesson 05 - Python String Formatting and Manipulation

This lesson covers various string formatting techniques in Python, from basic concatenation to modern f-strings and template strings, along with string manipulation methods.

## Learning Objectives

- Understand different string concatenation methods
- Master printf-style string formatting
- Learn the `.format()` method for string formatting
- Master f-string syntax (formatted string literals)
- Understand string joining techniques
- Learn string comparison and case manipulation
- Learn template strings (Python 3.14+)

## Course Content

### 01. String Concatenation
**File:** `01/concat.py`

Learn basic string concatenation techniques:

```python
#!/usr/bin/env python3

print('I have ' + str(12) + ' dollars')
# Output: I have 12 dollars

user = 'Alice'
money = 12
print(user + ' has ' + str(money) + ' dollars')
# Output: Alice has 12 dollars

print("Bob" " has " "12 dollars")
# Output: Bob has 12 dollars
```

**Key Concepts:**
- Basic string concatenation with `+` operator
- Converting numbers to strings with `str()`
- String literal concatenation (adjacent strings)
- Type conversion requirements for concatenation

### 02. Printf-Style Formatting
**File:** `02/printf_style.py`

Learn C-style string formatting with `%` operator:

```python
#!/usr/bin/env python3

print('Fill space to format output: %10s' % 'hello')

print('Fill zeros to format output: %04d' % 12)

print('Rounded output: %3.4f' % 3.14159)

print('%s have %d dollars' % ('I', 12))

print('%(user)s has %(money)d dollars' % {'user': 'Alice', 'money': 12})
```

**Key Concepts:**
- `%s` for string formatting
- `%d` for integer formatting
- `%f` for float formatting with precision
- Width and padding specifications
- Named placeholders with dictionaries
- Reference: [Printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

### 03. Format Method
**File:** `03/format.py`

Learn the `.format()` method for string formatting:

```python
#!/usr/bin/env python3

print('Fill space to format output: {:>10s}'.format('hello'))

print('Fill zeros to format output: {:04d}'.format(12))

print('{} have {} dollars'.format('I', 12))

print('{user} has {money} dollars'.format(user='Alice', money=12))

print('Reorder output: {0}. {2}, {1}'.format('Alice', 'Bob', 'Charlie'))
```

**Key Concepts:**
- `{}` placeholder syntax
- Format specification mini-language
- Named placeholders
- Positional argument indexing
- Alignment and padding options
- Reference: [Format Specification Mini-Language](https://docs.python.org/3.6/library/string.html#format-specification-mini-language)

### 04. F-Strings (Formatted String Literals)
**File:** `04/f-string.py`

Learn modern f-string syntax (Python 3.6+):

```python
#!/usr/bin/env python3

var = 'hello'
print(f'Fill space to format output: {var:>10}')

var = 12
print(f'Fill zeros to format output: {var+1:04}')

user = 'I'
money = 12
print(f'{user} have {money} dollars')

names = ['Alice', 'Bob', 'Charlie']
print(f'{names[0]} has {money} dollars')
```

**Key Concepts:**
- `f""` or `f''` prefix for f-strings
- Direct variable embedding `{variable}`
- Expression evaluation `{var+1}`
- Array/list access `{names[0]}`
- Format specifications `{var:>10}`
- Reference: [Formatted String Literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
- Reference: [PEP 498](https://www.python.org/dev/peps/pep-0498/)

### 05. String Joining
**File:** `05/join.py`

Learn efficient string joining with the `.join()` method:

```python
#!/usr/bin/env python3

names = ['Alice', 'Bob', 'Charlie']
print(', '.join(names))
```

**Key Concepts:**
- `.join()` method for combining multiple strings
- More efficient than repeated concatenation
- Separator string as the caller
- Working with iterables (lists, tuples, etc.)

### 06. String Comparison
**File:** `06/comparision.py`

Learn string comparison operations:

```python
#!/usr/bin/env python3

# Compare two strings
print('apple == apple:', 'apple' == 'apple')      # Output: True
print('apple < applepie:', 'apple' < 'applepie')  # Output: True
```

**Key Concepts:**
- String equality with `==` operator
- Lexicographical comparison with `<`, `>`, etc.
- ASCII/Unicode-based ordering
- Case-sensitive comparisons

### 07. Case Manipulation
**File:** `07/case.py`

Learn string case conversion methods:

```python
#!/usr/bin/env python3

test = "Hello"

print('test in lowercase:', test.lower())  # Output: hello
print('test in uppercase:', test.upper())  # Output: HELLO
```

**Key Concepts:**
- `.lower()` method for lowercase conversion
- `.upper()` method for uppercase conversion
- String immutability (methods return new strings)
- Other case methods: `.title()`, `.capitalize()`, `.swapcase()`

### 08. Template Strings (Python 3.14+)
**File:** `08/t-string.py`

Learn about the new template string literals:

```python
#!/usr/bin/env python3.14

name = "Alice"
age = 30
template = t"Hello, my name is {name} and I am {age} years old."
print(
    "".join(
        item if isinstance(item, str) else str(item.value)
        for item in template
    )
)
```

**Key Concepts:**
- `t""` prefix for template strings
- Template objects instead of immediate evaluation
- More flexible than f-strings for dynamic templating
- Template string iteration and processing
- Reference: [PEP 750 - Template String Literals](https://docs.python.org/3/whatsnew/3.14.html#pep-750-template-string-literals)

## String Formatting Comparison

| Method | Syntax | Python Version | Pros | Cons | Best For |
|--------|--------|----------------|------|------|----------|
| **Concatenation** | `'Hello ' + name` | All | Simple, intuitive | Inefficient, type conversion | Simple cases |
| **Printf-style** | `'Hello %s' % name` | All | Familiar to C developers | Limited functionality | Legacy code |
| **Format method** | `'Hello {}'.format(name)` | 2.6+ | Flexible, powerful | Verbose | Complex formatting |
| **F-strings** | `f'Hello {name}'` | 3.6+ | Readable, efficient | Requires newer Python | Modern code |
| **Template strings** | `t'Hello {name}'` | 3.14+ | Dynamic templating | Very new feature | Advanced templating |

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-05/01
python3 concat.py
```

```bash
cd lesson-0502
python3 printf_style.py
```

```bash
cd lesson-05/03
python3 format.py
```

```bash
cd lesson-05/04
python3 f-string.py
```

```bash
cd lesson-05/05
python3 join.py
```

```bash
cd lesson-05/06
python3 comparision.py
```

```bash
cd lesson-05/07
python3 case.py
```

```bash
# requires Python 3.14+
cd lesson-05/08
python3.14 t-string.py
```

**Note:** The `t-string.py` example requires Python 3.14 or later. If you're using an older version, you'll get a syntax error.

## Practice Suggestions

1. **Format Comparison**:
   - Rewrite the same output using all different formatting methods
   - Measure performance differences between methods
   - Test with different data types and complex formatting

2. **Real-world Applications**:
   - Create formatted reports with aligned columns
   - Build dynamic SQL queries using different methods
   - Format user-friendly error messages

3. **Advanced Formatting**:
   - Practice with number formatting (currency, percentages)
   - Work with date/time formatting
   - Experiment with alignment and padding options

4. **String Manipulation**:
   - Combine case methods with formatting
   - Practice string validation and sanitization
   - Work with multilingual text processing

## Performance Considerations

- **F-strings** are generally the fastest for simple formatting
- **Join method** is most efficient for combining many strings
- **Concatenation** with `+` can be slow for many operations
- **String formatting** is preferred over concatenation for readability

## Best Practices

1. **Use f-strings** for modern Python code (3.6+)
2. **Use .join()** when combining multiple strings
3. **Avoid repeated concatenation** in loops
4. **Consider template strings** for complex dynamic formatting
5. **Use appropriate precision** for floating-point numbers
6. **Be consistent** with formatting style within projects

## Related Resources

- [Python String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)
- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [PEP 498 - Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
- [PEP 750 - Template String Literals](https://docs.python.org/3/whatsnew/3.14.html#pep-750-template-string-literals)