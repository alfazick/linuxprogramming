# Linux Commands vs. Python Code: Explicit File and Directory Operations

This document compares common Linux commands for file and directory operations with their Python code equivalents, using explicit file operations. This comparison illustrates how the "Everything is a File" concept in Linux translates to programmatic operations in Python.

## 1. Creating a File

### Linux Command:
```bash
touch example.txt
```

### Python Code:
```python
# Create an empty file
f = open('example.txt', 'w')
f.close()

# Or create a file with content
f = open('example.txt', 'w')
f.write('Hello, Linux!')
f.close()
```

## 2. Writing to a File

### Linux Command:
```bash
echo "Hello, Linux!" > example.txt
```

### Python Code:
```python
f = open('example.txt', 'w')
f.write("Hello, Linux!")
f.close()
```

## 3. Reading from a File

### Linux Command:
```bash
cat example.txt
```

### Python Code:
```python
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()
```

## 4. Appending to a File

### Linux Command:
```bash
echo "This is a new line" >> example.txt
```

### Python Code:
```python
f = open('example.txt', 'a')
f.write("\nThis is a new line")
f.close()
```

## 5. Renaming a File

### Linux Command:
```bash
mv old_name.txt new_name.txt
```

### Python Code:
```python
import os
os.rename('old_name.txt', 'new_name.txt')
```

## 6. Removing a File

### Linux Command:
```bash
rm example.txt
```

### Python Code:
```python
import os
os.remove('example.txt')
```

## 7. Creating a Directory

### Linux Command:
```bash
mkdir new_directory
```

### Python Code:
```python
import os
os.mkdir('new_directory')
```

## 8. Listing Directory Contents

### Linux Command:
```bash
ls -l
```

### Python Code:
```python
import os
for item in os.listdir('.'):
    print(item)

# For more details, similar to ls -l:
import os
from datetime import datetime
for item in os.listdir('.'):
    stats = os.stat(item)
    print(f"{item:20} Size: {stats.st_size:10} Last modified: {datetime.fromtimestamp(stats.st_mtime)}")
```

## 9. Removing a Directory

### Linux Command:
```bash
rmdir empty_directory  # For empty directories
rm -r non_empty_directory  # For non-empty directories
```

### Python Code:
```python
import os
os.rmdir('empty_directory')  # For empty directories

import shutil
shutil.rmtree('non_empty_directory')  # For non-empty directories
```

## 10. Changing File Permissions

### Linux Command:
```bash
chmod 644 example.txt
```

### Python Code:
```python
import os
os.chmod('example.txt', 0o644)
```

These examples demonstrate how file and directory operations in Linux can be performed both through command-line instructions and Python code, illustrating the consistent interface provided by the "Everything is a File" philosophy.
