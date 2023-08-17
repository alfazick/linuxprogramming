# Lesson: Finding Files in Ubuntu Server Linux
**Duration**: 1 hour

## 1. Introduction
Searching for files effectively on a Linux system is a vital skill for any user, especially for system administrators and developers. Being able to pinpoint files based on various criteria can save a lot of time and hassle. In this lesson, we'll delve deep into two primary tools in Ubuntu Server Linux: `find` and `locate`.

## 2. Deep Dive into the `find` Command

### a. Basic Usage
The `find` command provides an extremely powerful and flexible method for locating files based on their properties, predominantly their names. It is designed to traverse directories recursively, ensuring no file is overlooked.

**Command**:
```bash
find ~ -name "*.txt"
```

Explanation: This command searches your entire home directory (~) for files ending with .txt.

### b. Using Criteria
The real power of find is in its ability to narrow down searches using various criteria.
**Command**:
By Name:
```bash
find /etc -name "*.conf"
Lists all files in the /etc directory and its subdirectories that end with .conf.
```
**Command**:
By Type:
```bash
find ~ -type d
```

Finds all directories within your home directory.
**Command**:
By Modification Time:
```bash
find /var/log -mtime -7
```

Finds files in /var/log modified in the last 7 days.
**Command**:
By Size:
```bash
find ~ -size +1M
```

Lists all files in the home directory larger than 1MB.

### c. Taking Actions
find isn't just for finding files; it can execute actions on the files it finds.

**Command**:
```bash
find . -name "*~" -exec rm {} \;
```

Explanation: This command finds all files ending with *~ in the current directory and its subdirectories and deletes them.

## 3. Introduction to locate and its Database
### a. Basic Usage
The locate command offers a speedy alternative to find by querying a pre-built database.

**Command**:
```bash
locate .conf
```

Explanation: Lists all files on your system containing .conf in their names.

### b. The Database behind locate
The speed of locate comes from its utilization of a periodically updated database.

**Command**:
```bash
sudo updatedb
```

Explanation: Updates the database that locate uses.


## 4. Advanced Tips
### a. Dealing with Special Characters
Filenames containing spaces or special characters can be tricky.

**Command**:
```bash
touch "test file.txt"
find . -name "test file.txt" -print0 | xargs -0 rm
```

Explanation: Demonstrates how to create a file with spaces in its name and then safely find and delete such files using find and xargs.

### b. Combining Multiple Criteria with find
**Command**:
```bash
find /etc -name "*.conf" -and -mtime -3
```
Explanation: Searches for .conf files in /etc that were modified in the last three days.

### c. Safety Tips
**Command**:
```bash
find ~ -name "*.bak" -ok rm {} \;
```
Explanation: Identifies .bak files and prompts for confirmation before deletion.
