# 1. Escape Characters
# Escape characters allow including special chars like newline (\n), tab (\t), backslash (\\), quotes (' or \"), etc.
# They start with a backslash \

print('Escape Examples:')
print('Line 1\n Line 2')  # \\n shows literal \n
print('Tab:\\t Tabbed')
print('Quotes: He said "Hello" or \'Hi\'')
print('Backslash: C:\\Users\\name')  # Raw string r'' avoids escapes
print(r'Raw: C:\Users\name')  # No interpretation

print('\\nNewline:')
print('Line 1\nLine 2')
print('\tTab:' + 'Tabbed'.expandtabs(4))
print('\tTab:' + 'Tabbed'.expandtabs(tabsize=4))
print('\\bBackspace effect:')
print('abc\\b')  # Moves cursor back

print('\n' + '='*50 + '\n')

# 2. Indexing and Slicing
# Strings are immutable sequences. Access by index (0-based), slice with [start:end:step]

s = 'Python Strings Tutorial'
print('String:', s)
print('Length:', len(s))

# Indexing
print('First char:', s[0])      # 'P'
print('Last char:', s[-1])      # 'l'
print('Second last:', s[-2])    # 'i'

# Slicing
print('Substring 0:6:', s[0:6])     # 'Python'
print('From index 7:', s[7:])       # 'Strings Tutorial'
print('Last 8 chars:', s[-8:])      # 'Tutorial'
print('Every 2nd char:', s[::2])    # 'Pto tigsTtoa'
print('Reverse:', s[::-1])          # 'lairoT sgnirtS nohtyP'
print('Step 3 from 1:', s[1::3])    # 'tosTuora'

print('\n' + '='*50 + '\n')

# 3. String Methods
# Strings have 100+ methods for manipulation. Immutable, so methods return new strings.

text = '  Python Programming  '
print('Original:', repr(text))

# Case
print('Upper:', text.upper())
print('Lower:', text.lower())
print('Title:', text.title())
print('Swapcase:', text.swapcase())

# Strip/Whitespace
print('Strip:', text.strip())
print('Lstrip:', text.lstrip())
print('Rstrip:', text.rstrip())

# Split/Join
words = text.split()
print('Split:', words)
print('Join with |:', '|'.join(words))
print('Join with space:', ' '.join(words))

# Replace
print('Replace P with J:', text.replace('P', 'J'))

# Find/Search
pos = text.find('Pro');
print('Find \"Pro\":', pos);
print('Contains \"Py\":', 'Py' in text);

# Start/End
print('Starts with space:', text.startswith(' '));
print('Ends with space:', text.endswith(' '));

# Other useful;
print('Count \"  \":', text.count(' '));
print('Center 30:', text.center(30, '-'));
print('Zfill:', text.zfill(30));

# Formatting example
name = 'Alice';
age = 30;
print(f'Hello, {name.upper()}! You are {age} years old.');
print('Splitlines:');
multiline = 'Line1\\nLine2';
print(repr(multiline.splitlines()));

print('\nChaining example:');
result = text.strip().upper().replace('PYTHON', 'Java').split();
print('Chained:', result);


# type 
# id
# str is immutable
# len is 
# count

