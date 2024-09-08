# Linux Basic Text Manipulation Commands Tutorial

This tutorial covers essential Linux commands for manipulating and analyzing text files, focusing solely on individual command usage.

## 1. cat - Concatenate and display file contents

The `cat` command is used to display the contents of files.

### Basic usage:
```bash
cat filename
```

### Examples:
```bash
# Display contents of a file
cat hello.txt

# Display file contents with line numbers
cat -n filename.txt
```

## 2. echo - Display messages or variables

The `echo` command prints text to the terminal.

### Basic usage:
```bash
echo "Your message here"
```

### Examples:
```bash
# Print a simple message
echo "Hello, World!"

# Print the value of a variable
NAME="Alice"
echo "My name is $NAME"
```

## 3. wc - Word, line, character, and byte count

The `wc` (word count) command is used to count lines, words, characters, or bytes in a file.

### Basic usage:
```bash
wc [options] filename
```

### Common options:
- `-l`: Count lines
- `-w`: Count words
- `-m`: Count characters
- `-c`: Count bytes

### Examples:
```bash
# Count lines in a file
wc -l filename.txt

# Count words in a file
wc -w filename.txt

# Display all counts (lines, words, characters)
wc filename.txt
```

## 4. sort - Sort lines of text

The `sort` command is used to sort lines of text alphabetically or numerically.

### Basic usage:
```bash
sort filename
```

### Examples:
```bash
# Sort lines alphabetically
sort names.txt

# Sort lines numerically
sort -n numbers.txt

# Sort in reverse order
sort -r filename.txt
```

## 5. grep - Search for patterns in files

The `grep` command searches for specific patterns in files.

### Basic usage:
```bash
grep "pattern" filename
```

### Examples:
```bash
# Search for a word in a file
grep "error" logfile.txt

# Case-insensitive search
grep -i "warning" logfile.txt

# Display line numbers with matches
grep -n "TODO" filename.txt
```

## 6. head - Display the beginning of a file

The `head` command shows the first part of a file, by default the first 10 lines.

### Basic usage:
```bash
head filename
```

### Examples:
```bash
# Display first 10 lines (default)
head filename.txt

# Display first 5 lines
head -n 5 filename.txt
```

## 7. tail - Display the end of a file

The `tail` command shows the last part of a file, by default the last 10 lines.

### Basic usage:
```bash
tail filename
```

### Examples:
```bash
# Display last 10 lines (default)
tail filename.txt

# Display last 20 lines
tail -n 20 filename.txt
```

These basic text manipulation commands provide powerful tools for working with text files in Linux. Each command can be used independently to perform specific tasks on text data.
