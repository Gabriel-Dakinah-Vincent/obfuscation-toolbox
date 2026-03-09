# Obfuscation Toolbox

[![CI](https://github.com/yourusername/obfuscation-toolbox/workflows/CI/badge.svg)](https://github.com/yourusername/obfuscation-toolbox/actions)
[![PyPI](https://img.shields.io/pypi/v/obfuscation-toolbox.svg)](https://pypi.org/project/obfuscation-toolbox/)
[![Python](https://img.shields.io/pypi/pyversions/obfuscation-toolbox.svg)](https://pypi.org/project/obfuscation-toolbox/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Professional Python code obfuscation library with 12+ techniques. Protect your source code from reverse engineering with industry-standard obfuscation methods.

## 🚀 Quick Start

### Installation

```bash
pip install obfuscation-toolbox
```

### Basic Usage

```python
from obfuscation_toolit import obfuscate, deobfuscate

# Obfuscate a string
code = "print('Hello, World!')"
obfuscated = obfuscate('string', code, level=2)
print(obfuscated)  # Output: cHJpbnQoJ0hlbGxvLCBXb3JsZCEnKQ==

# Deobfuscate it back
original = deobfuscate('string', obfuscated, level=2)
print(original)  # Output: print('Hello, World!')
```

## 📚 Table of Contents

- [Installation](#installation)
- [Available Methods](#available-methods)
- [Usage Guide](#usage-guide)
  - [Python API](#python-api)
  - [Command Line Interface](#command-line-interface)
- [Tutorial: Beginner to Advanced](#tutorial-beginner-to-advanced)
- [Real-World Scenarios](#real-world-scenarios)
- [Best Practices](#best-practices)
- [Security Considerations](#security-considerations)

## 🛠️ Available Methods

| Method | Description | Parameters | Reversible |
|--------|-------------|------------|------------|
| `string` | Base64 encoding | `level` (int): Encoding iterations | ✅ |
| `hex` | Hexadecimal encoding | None | ✅ |
| `xor` | XOR cipher encryption | `key` (int): XOR key | ✅ |
| `variable` | Variable renaming | `length` (int): Random name length | ⚠️ |
| `function_rename` | Function renaming | `length` (int): Random name length | ⚠️ |
| `class_rename` | Class renaming | `length` (int): Random name length | ⚠️ |
| `control_flow` | Dummy code injection | `complexity` (int): Dummy lines per line | ✅ |
| `comment` | Comment injection | `density` (int): Comments per line | ✅ |
| `minify` | Code minification | None | ⚠️ |
| `opaque_predicate` | Opaque predicates | `complexity` (int): Predicate count | ✅ |
| `dead_code` | Dead code insertion | `intensity` (int): Dead code lines | ✅ |
| `arithmetic` | Arithmetic obfuscation | None | ❌ |

⚠️ = Partial reversibility | ❌ = Not reversible

## 📖 Usage Guide

### Python API

#### Basic Obfuscation

```python
from obfuscation_toolit import obfuscate

# String encoding
code = "password = 'secret123'"
obfuscated = obfuscate('string', code, level=3)

# Variable renaming
code = "username = 'admin'\npassword = 'pass'"
obfuscated = obfuscate('variable', code, length=12)

# XOR encryption
code = "API_KEY = 'abc123'"
obfuscated = obfuscate('xor', code, key=255)
```

#### Combining Multiple Techniques

```python
from obfuscation_toolit import obfuscate

code = """
def authenticate(username, password):
    if username == 'admin' and password == 'secret':
        return True
    return False
"""

# Step 1: Rename functions
code = obfuscate('function_rename', code, length=10)

# Step 2: Rename variables
code = obfuscate('variable', code, length=8)

# Step 3: Add control flow obfuscation
code = obfuscate('control_flow', code, complexity=2)

# Step 4: Add dead code
code = obfuscate('dead_code', code, intensity=3)

print(code)
```

#### File Operations

```python
from obfuscation_toolit import obfuscate

# Read from file
with open('script.py', 'r') as f:
    code = f.read()

# Obfuscate
obfuscated = obfuscate('variable', code, length=10)

# Write to new file
with open('obfuscated_script.py', 'w') as f:
    f.write(obfuscated)
```

### Command Line Interface

#### List Available Methods

```bash
veil list
```

#### Obfuscate Text Directly

```bash
# String encoding
veil obfuscate string "print('hello')" --level 2

# XOR encryption
veil obfuscate xor "secret_data" --key 42

# Arithmetic obfuscation
veil obfuscate arithmetic "x = 100"
```

#### Obfuscate Files

```bash
# Basic file obfuscation
veil obfuscate variable --input-file script.py --output-file obfuscated.py --length 10

# Control flow obfuscation
veil obfuscate control_flow --input-file app.py --output-file app_obf.py --complexity 3

# Dead code insertion
veil obfuscate dead_code --input-file main.py --output-file main_obf.py --intensity 5
```

#### In-Place Modification

```bash
# Modify file directly (use with caution!)
veil obfuscate minify --input-file script.py --in-place
```

#### Deobfuscate Files

```bash
# Deobfuscate string
veil deobfuscate string --input-file obfuscated.txt --output-file original.txt --level 2

# Deobfuscate XOR
veil deobfuscate xor --input-file encrypted.txt --in-place --key 42
```

## 🎓 Tutorial: Beginner to Advanced

### Level 1: Beginner - Simple String Protection

**Goal**: Hide sensitive strings in your code

```python
from obfuscation_toolit import obfuscate, deobfuscate

# Original code with sensitive data
code = "API_KEY = 'sk_live_abc123xyz'"

# Method 1: Base64 encoding (easiest)
obfuscated = obfuscate('string', code, level=1)
print("Base64:", obfuscated)

# Method 2: Hex encoding
obfuscated = obfuscate('hex', code)
print("Hex:", obfuscated)

# Method 3: XOR encryption (more secure)
obfuscated = obfuscate('xor', code, key=123)
print("XOR:", obfuscated)

# Deobfuscate when needed
original = deobfuscate('xor', obfuscated, key=123)
print("Original:", original)
```

**Use Case**: Protecting API keys, passwords, or configuration strings.

### Level 2: Intermediate - Code Structure Obfuscation

**Goal**: Make code harder to understand by renaming identifiers

```python
from obfuscation_toolit import obfuscate

# Original readable code
code = """
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, username, email):
        user = {'name': username, 'email': email}
        self.users.append(user)
        return True
"""

# Step 1: Rename classes
step1 = obfuscate('class_rename', code, length=12)
print("After class rename:")
print(step1)

# Step 2: Rename functions
step2 = obfuscate('function_rename', step1, length=10)
print("\nAfter function rename:")
print(step2)

# Step 3: Rename variables
step3 = obfuscate('variable', step2, length=8)
print("\nFinal obfuscated:")
print(step3)
```

**Use Case**: Protecting intellectual property in distributed Python applications.

### Level 3: Advanced - Multi-Layer Protection

**Goal**: Maximum obfuscation using multiple techniques

```python
from obfuscation_toolit import obfuscate

# Complex business logic
code = """
def calculate_price(base_price, discount, tax_rate):
    discounted = base_price * (1 - discount)
    final_price = discounted * (1 + tax_rate)
    return final_price

result = calculate_price(100, 0.2, 0.15)
print(result)
"""

# Layer 1: Arithmetic obfuscation (hide numbers)
layer1 = obfuscate('arithmetic', code)
print("Layer 1 - Arithmetic:")
print(layer1)
print()

# Layer 2: Function renaming
layer2 = obfuscate('function_rename', layer1, length=15)
print("Layer 2 - Function rename:")
print(layer2)
print()

# Layer 3: Variable renaming
layer3 = obfuscate('variable', layer2, length=12)
print("Layer 3 - Variable rename:")
print(layer3)
print()

# Layer 4: Control flow obfuscation
layer4 = obfuscate('control_flow', layer3, complexity=2)
print("Layer 4 - Control flow:")
print(layer4)
print()

# Layer 5: Dead code insertion
layer5 = obfuscate('dead_code', layer4, intensity=3)
print("Layer 5 - Dead code:")
print(layer5)
print()

# Layer 6: Opaque predicates
final = obfuscate('opaque_predicate', layer5, complexity=2)
print("Final obfuscated code:")
print(final)
```

**Use Case**: Protecting proprietary algorithms, licensing systems, or anti-cheat mechanisms.

### Level 4: Expert - Automated Pipeline

**Goal**: Create a reusable obfuscation pipeline

```python
from obfuscation_toolit import obfuscate
import os

class ObfuscationPipeline:
    def __init__(self):
        self.techniques = []
    
    def add_technique(self, method, **params):
        self.techniques.append((method, params))
        return self
    
    def process(self, code):
        result = code
        for method, params in self.techniques:
            result = obfuscate(method, result, **params)
        return result
    
    def process_file(self, input_path, output_path):
        with open(input_path, 'r') as f:
            code = f.read()
        
        obfuscated = self.process(code)
        
        with open(output_path, 'w') as f:
            f.write(obfuscated)
        
        print(f"Obfuscated {input_path} -> {output_path}")

# Create pipeline
pipeline = ObfuscationPipeline()
pipeline.add_technique('arithmetic')
pipeline.add_technique('function_rename', length=12)
pipeline.add_technique('variable', length=10)
pipeline.add_technique('control_flow', complexity=2)
pipeline.add_technique('dead_code', intensity=3)

# Process single file
pipeline.process_file('app.py', 'app_obfuscated.py')

# Process entire directory
for filename in os.listdir('src'):
    if filename.endswith('.py'):
        input_path = os.path.join('src', filename)
        output_path = os.path.join('obfuscated', filename)
        pipeline.process_file(input_path, output_path)
```

**Use Case**: Production deployment, CI/CD integration, automated builds.

## 🌍 Real-World Scenarios

### Scenario 1: Protecting a Web Scraper

```python
from obfuscation_toolit import obfuscate

code = """
import requests

API_KEY = 'secret_key_12345'
BASE_URL = 'https://api.example.com'

def fetch_data(endpoint):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{BASE_URL}/{endpoint}', headers=headers)
    return response.json()
"""

# Protect API keys and URLs
protected = obfuscate('xor', code, key=77)
protected = obfuscate('function_rename', protected, length=10)
protected = obfuscate('variable', protected, length=8)

with open('scraper_protected.py', 'w') as f:
    f.write(protected)
```

### Scenario 2: License Key Validation

```python
from obfuscation_toolit import obfuscate

code = """
def validate_license(key):
    valid_keys = ['ABC-123-XYZ', 'DEF-456-UVW']
    return key in valid_keys

def check_expiry(license_key):
    expiry_date = '2025-12-31'
    # validation logic
    return True
"""

# Maximum protection for licensing logic
protected = obfuscate('arithmetic', code)
protected = obfuscate('function_rename', protected, length=15)
protected = obfuscate('variable', protected, length=12)
protected = obfuscate('control_flow', protected, complexity=3)
protected = obfuscate('opaque_predicate', protected, complexity=3)
protected = obfuscate('dead_code', protected, intensity=5)

with open('license_validator.py', 'w') as f:
    f.write(protected)
```

### Scenario 3: Configuration File Protection

```python
from obfuscation_toolit import obfuscate, deobfuscate
import json

# Sensitive configuration
config = {
    'database': 'postgresql://user:pass@localhost/db',
    'secret_key': 'django-secret-key-xyz',
    'api_keys': {'stripe': 'sk_live_abc', 'aws': 'AKIA123'}
}

# Convert to string and obfuscate
config_str = json.dumps(config)
obfuscated = obfuscate('xor', config_str, key=199)

# Save obfuscated config
with open('config.obf', 'w') as f:
    f.write(obfuscated)

# Load and deobfuscate at runtime
with open('config.obf', 'r') as f:
    obfuscated_data = f.read()

config_str = deobfuscate('xor', obfuscated_data, key=199)
config = json.loads(config_str)
print(config)
```

### Scenario 4: Distributing Python Tools

```bash
# Obfuscate before distribution
veil obfuscate variable --input-file mytool.py --output-file mytool_dist.py --length 15
veil obfuscate control_flow --input-file mytool_dist.py --in-place --complexity 3
veil obfuscate dead_code --input-file mytool_dist.py --in-place --intensity 4

# Package and distribute
python setup.py sdist bdist_wheel
```

## ✅ Best Practices

### 1. Choose the Right Technique

```python
# For strings and data: Use XOR or Base64
obfuscate('xor', sensitive_data, key=42)

# For code structure: Use renaming
obfuscate('variable', code, length=10)

# For maximum protection: Combine multiple techniques
```

### 2. Keep Obfuscation Keys Secure

```python
# ❌ BAD: Hardcoded key in source
key = 42
obfuscated = obfuscate('xor', data, key=key)

# ✅ GOOD: Key from environment
import os
key = int(os.environ.get('OBFUSCATION_KEY', 42))
obfuscated = obfuscate('xor', data, key=key)
```

### 3. Test Obfuscated Code

```python
# Always verify obfuscated code works
original_code = "x = 5\nprint(x)"
obfuscated = obfuscate('variable', original_code, length=8)

# Test execution
try:
    exec(obfuscated)
    print("✅ Obfuscated code works")
except Exception as e:
    print(f"❌ Error: {e}")
```

### 4. Version Control Strategy

```bash
# Keep original source in private repo
git add src/

# Obfuscate for public distribution
veil obfuscate variable --input-file src/app.py --output-file dist/app.py --length 12

# Only commit obfuscated version to public repo
cd public-repo
git add dist/
git commit -m "Release obfuscated version"
```

### 5. Performance Considerations

```python
# Obfuscation adds overhead - measure impact
import time

original = "x = sum(range(1000))"
obfuscated = obfuscate('arithmetic', original)

start = time.time()
exec(original)
original_time = time.time() - start

start = time.time()
exec(obfuscated)
obfuscated_time = time.time() - start

print(f"Overhead: {(obfuscated_time/original_time - 1) * 100:.2f}%")
```

### 6. Layered Security

```python
# Combine obfuscation with other security measures
from obfuscation_toolit import obfuscate
import hashlib

code = "secret_algorithm()"

# Layer 1: Obfuscate
obfuscated = obfuscate('variable', code, length=10)

# Layer 2: Add integrity check
checksum = hashlib.sha256(obfuscated.encode()).hexdigest()

# Layer 3: Encrypt if needed
# Use proper encryption library for sensitive data
```

### 7. Documentation

```python
# Document your obfuscation strategy
"""
Obfuscation Strategy:
- Technique: variable + control_flow + dead_code
- Parameters: length=12, complexity=3, intensity=4
- Key storage: Environment variable OBFUSCATION_KEY
- Deobfuscation: Not required for production
- Last updated: 2024-01-15
"""
```

## 🔒 Security Considerations

### Important Warnings

1. **Obfuscation ≠ Encryption**: Obfuscation provides obscurity, not cryptographic security
2. **Reversible**: Most techniques can be reversed with enough effort
3. **Not for Secrets**: Don't rely solely on obfuscation for protecting sensitive data
4. **Performance**: Obfuscation adds runtime overhead
5. **Maintenance**: Obfuscated code is harder to debug and maintain

### When to Use Obfuscation

✅ **Good Use Cases:**
- Protecting intellectual property
- Making reverse engineering harder
- Hiding business logic
- Anti-tampering measures
- License validation systems

❌ **Bad Use Cases:**
- Storing passwords (use proper hashing)
- Protecting cryptographic keys (use key management)
- Securing API tokens (use environment variables)
- Hiding security vulnerabilities

### Recommended Security Stack

```python
# 1. Proper encryption for sensitive data
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(b"sensitive_data")

# 2. Obfuscation for code protection
from obfuscation_toolit import obfuscate
obfuscated_code = obfuscate('variable', code, length=12)

# 3. Environment variables for configuration
import os
api_key = os.environ.get('API_KEY')

# 4. Code signing for integrity
# Use tools like sigstore or GPG
```

## 📦 Integration Examples

### CI/CD Pipeline (GitHub Actions)

```yaml
name: Build and Obfuscate

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: pip install veilbox
      - name: Obfuscate code
        run: |
          veil obfuscate variable --input-file src/app.py --output-file dist/app.py --length 12
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: obfuscated-code
          path: dist/
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

veil obfuscate variable --input-file src/main.py --output-file dist/main.py --length 10
git add dist/main.py
```

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and legitimate purposes only. Users are responsible for compliance with applicable laws and regulations. Obfuscation should not be used to hide malicious code or violate software licenses.

## 🔗 Resources

- [Documentation](https://github.com/yourusername/obfuscation-toolbox/wiki)
- [Issue Tracker](https://github.com/yourusername/obfuscation-toolbox/issues)
- [Changelog](CHANGELOG.md)

---

## 📋 Detailed Techniques Reference

### 1. String Obfuscation (`string`)
- **Description**: Base64 encoding with multiple levels
- **Parameters**: `level` (int) - Number of encoding iterations
- **Use Case**: Hide string literals
- **Example**: `obfuscate('string', "hello", level=2)`

### 2. Hex Encoding (`hex`)
- **Description**: Hexadecimal encoding
- **Parameters**: None
- **Use Case**: Simple string encoding
- **Example**: `obfuscate('hex', "hello")`

### 3. XOR Encoding (`xor`)
- **Description**: XOR cipher with custom key
- **Parameters**: `key` (int) - XOR key value
- **Use Case**: Symmetric encryption
- **Example**: `obfuscate('xor', "hello", key=42)`

### 4. Variable Renaming (`variable`)
- **Description**: Rename all variables to random strings
- **Parameters**: `length` (int) - Length of random names
- **Use Case**: Hide variable names
- **Example**: `obfuscate('variable', "x = 5", length=10)`

### 5. Function Renaming (`function_rename`)
- **Description**: Rename all functions to random strings
- **Parameters**: `length` (int) - Length of random names
- **Use Case**: Hide function names
- **Example**: `obfuscate('function_rename', "def test(): pass", length=10)`

### 6. Class Renaming (`class_rename`)
- **Description**: Rename all classes to random strings
- **Parameters**: `length` (int) - Length of random names
- **Use Case**: Hide class names
- **Example**: `obfuscate('class_rename', "class MyClass: pass", length=10)`

### 7. Control Flow Obfuscation (`control_flow`)
- **Description**: Insert dummy code between lines
- **Parameters**: `complexity` (int) - Dummy lines per line
- **Use Case**: Confuse control flow analysis
- **Example**: `obfuscate('control_flow', "x = 1", complexity=3)`

### 8. Comment Injection (`comment`)
- **Description**: Insert random comments
- **Parameters**: `density` (int) - Comments per line
- **Use Case**: Add noise to code
- **Example**: `obfuscate('comment', "x = 1", density=2)`

### 9. Code Minification (`minify`)
- **Description**: Remove whitespace and comments
- **Parameters**: None
- **Use Case**: Reduce code size
- **Example**: `obfuscate('minify', "x = 5\\ny = 10")`

### 10. Opaque Predicates (`opaque_predicate`)
- **Description**: Insert always-true/false conditions
- **Parameters**: `complexity` (int) - Predicate count
- **Use Case**: Confuse static analysis
- **Example**: `obfuscate('opaque_predicate', "x = 1", complexity=2)`

### 11. Dead Code Insertion (`dead_code`)
- **Description**: Insert unreachable code
- **Parameters**: `intensity` (int) - Dead code lines
- **Use Case**: Add noise and confusion
- **Example**: `obfuscate('dead_code', "x = 1", intensity=3)`

### 12. Arithmetic Obfuscation (`arithmetic`)
- **Description**: Replace numbers with arithmetic expressions
- **Parameters**: None
- **Use Case**: Hide numeric constants
- **Example**: `obfuscate('arithmetic', "x = 5")`

---

## 🔄 Deobfuscation Capabilities

### Fully Reversible ✅

**These techniques perfectly restore the original code:**

1. **String** - `deobfuscate('string', obfuscated, level=2)`
2. **Hex** - `deobfuscate('hex', obfuscated)`
3. **XOR** - `deobfuscate('xor', obfuscated, key=42)` (requires same key)
4. **Control Flow** - `deobfuscate('control_flow', obfuscated, complexity=2)`
5. **Comment** - `deobfuscate('comment', obfuscated, density=2)`
6. **Dead Code** - `deobfuscate('dead_code', obfuscated, intensity=3)`
7. **Opaque Predicates** - `deobfuscate('opaque_predicate', obfuscated, complexity=2)`
8. **Minify** - `deobfuscate('minify', obfuscated)` (restores structure)

### Partially Reversible ⚠️

**These require the same obfuscator instance (not cross-session):**

9. **Variable** - Requires same instance with mapping
10. **Function Rename** - Requires same instance with mapping
11. **Class Rename** - Requires same instance with mapping

```python
# Same-session deobfuscation example
from obfuscation_toolit.techniques.variable import VariableObfuscator

obfuscator = VariableObfuscator(length=10)
obfuscated = obfuscator.obfuscate("x = 5")
deobfuscated = obfuscator.deobfuscate(obfuscated)  # Works!
```

### Not Reversible ❌

12. **Arithmetic** - Intentionally irreversible (numbers become expressions)

```python
# Arithmetic is one-way
code = "x = 5"
obfuscated = obfuscate('arithmetic', code)
# Result: "x = (9 - 4)" or similar
# Cannot reverse to original "5"
```
