# Lesson 15 - HTTP Client Programming  <!-- omit in toc -->

This lesson covers comprehensive HTTP client programming in Python using both urllib (built-in) and requests (third-party) libraries, from basic web requests to advanced HTTP client applications.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. urllib - Built-in HTTP Client](#01-urllib---built-in-http-client)
  - [02. requests - Elegant HTTP Client](#02-requests---elegant-http-client)
- [HTTP Methods and Operations](#http-methods-and-operations)
  - [urllib HTTP Methods](#urllib-http-methods)
    - [GET Requests](#get-requests)
    - [POST Requests](#post-requests)
    - [Custom Headers](#custom-headers)
  - [requests HTTP Methods](#requests-http-methods)
    - [GET Requests](#get-requests-1)
    - [POST Requests](#post-requests-1)
    - [Other HTTP Methods](#other-http-methods)
- [Advanced HTTP Client Features](#advanced-http-client-features)
  - [Headers and Authentication](#headers-and-authentication)
    - [Custom Headers](#custom-headers-1)
    - [Basic Authentication](#basic-authentication)
    - [Bearer Token Authentication](#bearer-token-authentication)
  - [Sessions and Cookies](#sessions-and-cookies)
    - [Using Sessions](#using-sessions)
    - [Manual Cookie Handling](#manual-cookie-handling)
  - [Error Handling and Timeouts](#error-handling-and-timeouts)
    - [Comprehensive Error Handling](#comprehensive-error-handling)
    - [Status Code Handling](#status-code-handling)
- [Practical HTTP Client Examples](#practical-http-client-examples)
  - [API Client Class](#api-client-class)
  - [File Download with Progress](#file-download-with-progress)
  - [Web Scraping Example](#web-scraping-example)
- [How to Run Examples](#how-to-run-examples)
  - [Basic urllib Example](#basic-urllib-example)
  - [requests Example](#requests-example)
- [Library Comparison](#library-comparison)
  - [urllib vs requests](#urllib-vs-requests)
  - [When to Use Each](#when-to-use-each)
    - [Choose urllib when:](#choose-urllib-when)
    - [Choose requests when:](#choose-requests-when)
- [Best Practices](#best-practices)
  - [1. **Always Handle Errors**](#1-always-handle-errors)
  - [2. **Use Sessions for Multiple Requests**](#2-use-sessions-for-multiple-requests)
  - [3. **Set Appropriate Timeouts**](#3-set-appropriate-timeouts)
  - [4. **Use Appropriate HTTP Methods**](#4-use-appropriate-http-methods)
  - [5. **Validate and Sanitize Input**](#5-validate-and-sanitize-input)
- [Advanced Topics](#advanced-topics)
  - [Asynchronous HTTP Requests](#asynchronous-http-requests)
  - [HTTP/2 Support with httpx](#http2-support-with-httpx)
  - [Custom SSL/TLS Configuration](#custom-ssltls-configuration)
- [Common HTTP Status Codes](#common-http-status-codes)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Master Python's built-in urllib module
- Learn requests library for elegant HTTP operations
- Understand HTTP methods and status codes
- Handle HTTP headers and parameters
- Manage cookies and sessions
- Work with authentication mechanisms
- Handle errors and timeouts gracefully
- Build robust HTTP client applications

## Course Content

### 01. urllib - Built-in HTTP Client
**File:** `01/main.py`

Learn HTTP requests with Python's built-in urllib module:

```python
#!/usr/bin/env python3

from urllib import request

def fetch_url(url: str) -> str:
    with request.urlopen(url) as response:
        return response.read().decode('utf-8')

if __name__ == '__main__':
    url = 'http://www.google.com'
    content = fetch_url(url)
    print(content)
```

**Key Concepts:**
- `urllib.request.urlopen()` for making HTTP requests
- Context manager for automatic resource cleanup
- Response decoding from bytes to string
- Basic GET request functionality
- Built-in library, no external dependencies

### 02. requests - Elegant HTTP Client
**Files:** `02/main.py`, `02/requirements.txt`

Learn modern HTTP client programming with the requests library:

**Requirements (`02/requirements.txt`)**
```pip-requirements
requests
```

**Application Code (`02/main.py`)**
```python
#!/usr/bin/env python3

import requests

def fetch_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

if __name__ == '__main__':
    url = 'http://www.google.com'
    content = fetch_url(url)
    print(content)
```

**Key Concepts:**
- `requests.get()` for simple HTTP GET requests
- `response.raise_for_status()` for error handling
- Automatic content decoding with `response.text`
- More intuitive API than urllib
- Third-party dependency required

## HTTP Methods and Operations

### urllib HTTP Methods

#### GET Requests
```python
from urllib import request
from urllib.parse import urlencode

# Simple GET request
with request.urlopen('https://api.example.com/data') as response:
    data = response.read().decode('utf-8')

# GET with parameters
params = {'q': 'python', 'limit': 10}
url = f'https://api.example.com/search?{urlencode(params)}'
with request.urlopen(url) as response:
    data = response.read().decode('utf-8')
```

#### POST Requests
```python
from urllib import request
import json

# POST with data
data = json.dumps({'name': 'John', 'age': 30}).encode('utf-8')
req = request.Request('https://api.example.com/users',
                     data=data,
                     headers={'Content-Type': 'application/json'})

with request.urlopen(req) as response:
    result = response.read().decode('utf-8')
```

#### Custom Headers
```python
from urllib import request

req = request.Request('https://api.example.com/data')
req.add_header('User-Agent', 'Python-urllib/3.11')
req.add_header('Authorization', 'Bearer your-token-here')

with request.urlopen(req) as response:
    data = response.read().decode('utf-8')
```

### requests HTTP Methods

#### GET Requests
```python
import requests

# Simple GET request
response = requests.get('https://api.example.com/data')
response.raise_for_status()
data = response.text

# GET with parameters
params = {'q': 'python', 'limit': 10}
response = requests.get('https://api.example.com/search', params=params)
data = response.json()  # Automatic JSON parsing
```

#### POST Requests
```python
import requests

# POST with JSON data
data = {'name': 'John', 'age': 30}
response = requests.post('https://api.example.com/users', json=data)
response.raise_for_status()

# POST with form data
form_data = {'username': 'john', 'password': 'secret'}
response = requests.post('https://api.example.com/login', data=form_data)
```

#### Other HTTP Methods
```python
import requests

# PUT request
response = requests.put('https://api.example.com/users/1', json={'name': 'Jane'})

# DELETE request
response = requests.delete('https://api.example.com/users/1')

# PATCH request
response = requests.patch('https://api.example.com/users/1', json={'age': 31})

# HEAD request (headers only)
response = requests.head('https://api.example.com/users/1')
```

## Advanced HTTP Client Features

### Headers and Authentication

#### Custom Headers
```python
import requests

headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer your-token-here'
}

response = requests.get('https://api.example.com/data', headers=headers)
```

#### Basic Authentication
```python
import requests
from requests.auth import HTTPBasicAuth

# Method 1: Using auth parameter
response = requests.get('https://api.example.com/data',
                       auth=HTTPBasicAuth('username', 'password'))

# Method 2: Using tuple shorthand
response = requests.get('https://api.example.com/data',
                       auth=('username', 'password'))
```

#### Bearer Token Authentication
```python
import requests

headers = {'Authorization': 'Bearer your-jwt-token-here'}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Sessions and Cookies

#### Using Sessions
```python
import requests

# Session maintains cookies and connection pooling
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Login and store cookies
login_data = {'username': 'john', 'password': 'secret'}
session.post('https://example.com/login', data=login_data)

# Subsequent requests use stored cookies
response = session.get('https://example.com/protected')

session.close()  # Clean up
```

#### Manual Cookie Handling
```python
import requests

# Send cookies
cookies = {'session_id': 'abc123', 'user_pref': 'dark_mode'}
response = requests.get('https://example.com/data', cookies=cookies)

# Access response cookies
print(response.cookies['new_session_id'])
```

### Error Handling and Timeouts

#### Comprehensive Error Handling
```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def safe_request(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except Timeout:
        print(f"Request to {url} timed out")
    except ConnectionError:
        print(f"Failed to connect to {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except RequestException as e:
        print(f"Request failed: {e}")
    return None
```

#### Status Code Handling
```python
import requests

response = requests.get('https://api.example.com/data')

if response.status_code == 200:
    print("Success!")
    data = response.json()
elif response.status_code == 404:
    print("Resource not found")
elif response.status_code == 401:
    print("Unauthorized")
elif response.status_code >= 500:
    print("Server error")
else:
    print(f"Unexpected status code: {response.status_code}")
```

## Practical HTTP Client Examples

### API Client Class
```python
import requests
from typing import Dict, Any, Optional
import json

class APIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        response = self._make_request('GET', endpoint, params=params)
        return response.json()

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._make_request('POST', endpoint, json=data)
        return response.json()

    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._make_request('PUT', endpoint, json=data)
        return response.json()

    def delete(self, endpoint: str) -> bool:
        response = self._make_request('DELETE', endpoint)
        return response.status_code == 204

    def close(self):
        self.session.close()

# Usage
client = APIClient('https://api.example.com', api_key='your-key')
try:
    users = client.get('/users', params={'limit': 10})
    new_user = client.post('/users', {'name': 'John', 'email': 'john@example.com'})
    print(f"Created user: {new_user}")
finally:
    client.close()
```

### File Download with Progress
```python
import requests
from pathlib import Path

def download_file(url: str, filename: str, chunk_size: int = 8192):
    """Download file with progress indicator"""
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded += len(chunk)

                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"\rDownloading: {percent:.1f}%", end='', flush=True)

    print(f"\nDownload completed: {filename}")

# Usage
download_file('https://example.com/large-file.zip', 'downloaded-file.zip')
```

### Web Scraping Example
```python
import requests
from urllib.parse import urljoin, urlparse
import re

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; WebScraper/1.0)'
        })

    def get_page(self, url: str) -> str:
        """Fetch page content"""
        response = self.session.get(url)
        response.raise_for_status()
        return response.text

    def extract_links(self, html: str, base_url: str) -> list:
        """Extract all links from HTML"""
        link_pattern = r'<a[^>]+href=["\']([^"\']+)["\']'
        links = re.findall(link_pattern, html, re.IGNORECASE)

        # Convert relative URLs to absolute
        absolute_links = []
        for link in links:
            absolute_url = urljoin(base_url, link)
            absolute_links.append(absolute_url)

        return absolute_links

    def scrape_site(self, start_url: str, max_pages: int = 10):
        """Scrape website starting from given URL"""
        visited = set()
        to_visit = [start_url]

        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            if url in visited:
                continue

            try:
                print(f"Scraping: {url}")
                html = self.get_page(url)
                visited.add(url)

                # Extract and queue new links
                links = self.extract_links(html, url)
                for link in links:
                    if urlparse(link).netloc == urlparse(start_url).netloc:
                        to_visit.append(link)

            except requests.RequestException as e:
                print(f"Error scraping {url}: {e}")

    def close(self):
        self.session.close()

# Usage
scraper = WebScraper()
try:
    scraper.scrape_site('https://example.com', max_pages=5)
finally:
    scraper.close()
```

## How to Run Examples

### Basic urllib Example
```bash
# Navigate to corresponding directory
cd lesson-15/01
python3 main.py
```

### requests Example
```bash
cd lesson-15/02

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the script
python3 main.py
```

## Library Comparison

### urllib vs requests

| Feature | urllib | requests |
|---------|--------|----------|
| **Installation** | Built-in | Third-party |
| **API Simplicity** | Complex | Simple |
| **JSON Support** | Manual | Automatic |
| **Session Support** | Manual | Built-in |
| **Cookie Handling** | Manual | Automatic |
| **Authentication** | Manual | Built-in |
| **Error Handling** | Basic | Comprehensive |
| **Connection Pooling** | No | Yes |
| **HTTP/2 Support** | No | With httpx |

### When to Use Each

#### Choose urllib when:
- No external dependencies allowed
- Simple GET requests only
- Minimal HTTP client needs
- Educational purposes
- System programming

#### Choose requests when:
- Building production applications
- Need advanced HTTP features
- Want clean, readable code
- Working with APIs regularly
- Rapid development required

## Best Practices

### 1. **Always Handle Errors**
```python
# Good: Comprehensive error handling
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# Avoid: No error handling
response = requests.get(url)
return response.json()  # Could fail silently
```

### 2. **Use Sessions for Multiple Requests**
```python
# Good: Use session for multiple requests
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})

for url in urls:
    response = session.get(url)
    process_response(response)

session.close()

# Avoid: Creating new connections for each request
for url in urls:
    response = requests.get(url)  # New connection each time
```

### 3. **Set Appropriate Timeouts**
```python
# Good: Always set timeouts
response = requests.get(url, timeout=(5, 30))  # (connect, read) timeout

# Good: Different timeouts for different operations
response = requests.get(url, timeout=5)        # Quick API call
response = requests.get(large_file_url, timeout=300)  # File download

# Avoid: No timeout (could hang forever)
response = requests.get(url)
```

### 4. **Use Appropriate HTTP Methods**
```python
# Good: Use correct HTTP methods
response = requests.get('/api/users')      # Retrieve data
response = requests.post('/api/users', json=data)  # Create resource
response = requests.put('/api/users/1', json=data) # Update resource
response = requests.delete('/api/users/1')  # Delete resource

# Avoid: Using GET for everything
response = requests.get('/api/delete-user?id=1')  # Should be DELETE
```

### 5. **Validate and Sanitize Input**
```python
# Good: Validate URLs and parameters
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

if is_valid_url(user_provided_url):
    response = requests.get(user_provided_url)

# Good: Sanitize parameters
params = {k: str(v)[:100] for k, v in user_params.items()}  # Limit length
```

## Advanced Topics

### Asynchronous HTTP Requests
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error: {e}"

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
urls = ['http://example.com', 'http://google.com', 'http://github.com']
results = asyncio.run(fetch_multiple_urls(urls))
```

### HTTP/2 Support with httpx
```python
import httpx

# HTTP/2 support
with httpx.Client(http2=True) as client:
    response = client.get('https://httpbin.org/get')
    print(f"HTTP version: {response.http_version}")

# Async HTTP/2
async with httpx.AsyncClient(http2=True) as client:
    response = await client.get('https://httpbin.org/get')
    print(response.json())
```

### Custom SSL/TLS Configuration
```python
import requests
import ssl

# Disable SSL verification (not recommended for production)
response = requests.get('https://example.com', verify=False)

# Custom CA bundle
response = requests.get('https://example.com', verify='/path/to/ca-bundle.crt')

# Custom SSL context with urllib
import urllib.request
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen('https://example.com', context=context) as response:
    data = response.read()
```

## Common HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid request syntax |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 502 | Bad Gateway | Proxy error |
| 503 | Service Unavailable | Server overloaded |

## Practice Suggestions

1. **API Client Library**: Build a client for a public API (GitHub, Twitter, etc.)
2. **Web Scraper**: Create a scraper for news websites or job boards
3. **File Downloader**: Build a multi-threaded file downloader
4. **HTTP Monitoring Tool**: Monitor website uptime and response times
5. **REST API Tester**: Create a tool to test REST API endpoints
6. **Webhook Handler**: Build a service to receive and process webhooks

## Common Pitfalls

- **Not handling timeouts**: Always set appropriate timeouts
- **Ignoring HTTP status codes**: Check status codes and handle errors
- **Not using sessions**: Use sessions for multiple requests to same host
- **Hardcoding URLs**: Use configuration files or environment variables
- **No rate limiting**: Respect API rate limits and implement backoff
- **Security issues**: Validate inputs and use HTTPS when possible
- **Memory issues**: Use streaming for large files

## Related Resources

- [urllib Documentation](https://docs.python.org/3/library/urllib.html)
- [requests Documentation](https://requests.readthedocs.io/)
- [httpx Documentation](https://www.python-httpx.org/) - Modern async HTTP client
- [aiohttp Documentation](https://docs.aiohttp.org/) - Async HTTP client/server
- [HTTP Status Codes](https://httpstatuses.com/)
- [REST API Best Practices](https://restfulapi.net/)