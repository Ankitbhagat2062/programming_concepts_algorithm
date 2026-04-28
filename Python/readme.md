# Python Strings Tutorial

## 1. Escape Characters
Escape characters (`\\`) insert special characters:
- `\\n`: Newline
- `\\t`: Tab
- `\\\\`: Backslash
- `\\'`: Single quote
- `\\\"`: Double quote
- `\\r`: Carriage return
- `\\b`: Backspace

**Example:**
```python
print('Hello\\nWorld')  # Shows: Hello\nWorld
print(r'Raw: C:\\Users') # Raw string ignores escapes
```

**Output:**
```
Hello\nWorld
Raw: C:\Users
```

## 2. Indexing and Slicing
Strings are sequences: `s[index]` or `s[start:end:step]`.
- Positive index: left-to-right (0...)
- Negative: right-to-left (-1...)
- Slice excludes `end`.

**Example:**
```python
s = 'Python'
print(s[0])     # 'P'
print(s[-1])    # 'n'
print(s[1:4])   # 'yth'
print(s[::-1])  # 'nohtyP'
```

## 3. String Methods
Immutable methods return new strings. Key ones:

| Method | Description | Example |
|--------|-------------|---------|
| `upper()`, `lower()` | Case change | `'hello'.upper()` → `'HELLO'` |
| `strip()`, `lstrip()`, `rstrip()` | Remove whitespace | `'  hi  '.strip()` → `'hi'` |
| `split(sep)`, `join(iter)` | Split/Join | `'a b c'.split()` → `['a','b','c']`<br>`'-'.join(['a','b'])` → `'a-b'` |
| `replace(old, new)` | Replace | `'hi'.replace('h','H')` → `'Hi'` |
| `find(sub)` | Index of sub | `'hello'.find('l')` → `2` |
| `startswith()`, `endswith()` | Prefix/Suffix check | `'hello'.startswith('he')` → `True` |
| `count(sub)` | Count occurrences | `'aaa'.count('a')` → `3` |

**Run full demo:**
```bash
run_demo.bat
```

**Chaining:**
```python
('  hello  '.strip().upper().replace('HELLO', 'HI'))
# → 'HI'
```

See `strings_demo.py` for complete runnable code.





Write a program that takes two number and prints the result of all 7 airthmatic operations (+,-,/,*,//,**,%)