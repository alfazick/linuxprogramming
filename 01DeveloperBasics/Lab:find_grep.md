# Lab Assignments on `find` Command

## Objective
Understand the practical applications of the `find` command in locating files based on various criteria.

### **Exercise 1: Finding Files by Modification Time**
1. Navigate to the `/tmp` directory.
2. Create a new file named `tstfile` using the `touch` command.
3. After a few minutes, create a few more files in the `/tmp` directory.
4. Use the `find` command to list all files under the `/tmp` directory that are newer than `tstfile`:
```bash
$ find /tmp -newer /tmp/tstfile -ls
```

### **Exercise 2: Locating Configuration Files**
1. Use the `find` command to locate all files under the `/etc` directory with a `.conf` extension:
```bash
$ find /etc -name "*.conf"
```

### **Exercise 3: Finding Directories**
1. Identify all subdirectories under the `/etc` directory using:
```bash
$ find /etc -type d
```

### **Exercise 4: Deleting Backup Files**
**Warning**: Be cautious with this exercise, as it involves file deletion.
1. Use the `find` command to locate all `.bak` files on the system.
2. Once you're sure of the files you're targeting, append the `-delete` option to the `find` command to remove them.

---

# Lab Assignments on `grep` Command

## Objective
Develop a strong understanding of the `grep` command's capabilities in searching patterns within files.

### **Exercise 1: Searching for a Pattern**
1. Use the `grep` command to locate all entries in the `/etc/services` file that include the string `ftp`:
```bash
$ grep ftp /etc/services
```

### **Exercise 2: Filtering by Protocol**
1. Further refine your search from Exercise 1 to only include services using the `tcp` protocol:
```bash
$ grep ftp /etc/services | grep tcp
```

### **Exercise 3: Excluding a Protocol with Line Numbers**
1. Modify the search to exclude services using the `tcp` protocol and print the line numbers:
```bash
$ grep -n ftp /etc/services | grep -v tcp
```

### **Exercise 4: Using Regular Expressions**
1. Use the `grep` command to locate strings in `/etc/services` that either start with `ts` or end with `st`:
```bash
$ grep '^ts\|st$' /etc/services
```

---

After completing these lab exercises, you should have a deeper understanding of the capabilities and usage scenarios for both the `find` and `grep` commands. Always remember to be cautious, especially when performing actions like deleting files or making modifications.

