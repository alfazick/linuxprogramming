# Linux File Structure Manipulation Lab

## Introduction

This lab is designed to help you practice creating and manipulating file structures in Linux. You'll learn how to create directories, files, and verify your work using the `tree` command. We'll also explore concepts like hidden files and simulate a Git-initialized project structure.

## Prerequisites

- Access to a Linux terminal
- Basic knowledge of command-line operations
- The `tree` command installed (if not installed, you can use `find` as an alternative)

## Warm Up Assignment: Create a Simple File and Folder Structure

### Objectives
- Create a directory structure that includes a couple of sub-directories.
- Create some files within these directories.
- Use the tree command to verify your work.

### Steps
1. Open a terminal.

2. Create a root directory for your assignment and navigate into it:
   ```
   mkdir AssignmentRoot
   cd AssignmentRoot
   ```

3. Create two sub-directories within AssignmentRoot:
   ```
   mkdir SubDir1 SubDir2
   ```

4. Navigate into SubDir1 and create a file:
   ```
   cd SubDir1
   touch file1.txt
   cd ..
   ```

5. Navigate into SubDir2 and create another file:
   ```
   cd SubDir2
   touch file2.txt
   cd ..
   ```

6. Display the tree structure listing of AssignmentRoot and its contents:
   ```
   tree AssignmentRoot
   ```

   Note: If the tree command is not installed, you can install it using:
   ```
   sudo apt install tree
   ```

   Alternatively, you can use the find command:
   ```
   find AssignmentRoot
   ```

## Assignment 1: Set Up a Basic Programming Project

### Objective
Create a basic project directory structure.

### Folder and File Structure
```
MyProject1/
│
├── Images/
│   ├── logo.png
│   └── banner.png
│
├── Code/
│   ├── main.py
│   └── utils.py
│
└── Configs/
    └── settings.conf
```

### Steps
1. Create the project structure:
   ```
   mkdir -p MyProject1/{Images,Code,Configs}
   touch MyProject1/Images/{logo.png,banner.png}
   touch MyProject1/Code/{main.py,utils.py}
   touch MyProject1/Configs/settings.conf
   ```

2. Verify the structure:
   ```
   tree MyProject1
   ```

## Assignment 2: Hidden Files in Project

### Objective
Introduce hidden configuration files to your project structure.

### Folder and File Structure
```
MyProject2/
│
├── Images/
│
├── Code/
│
├── Configs/
│   └── .secret_key
│
├── .config
│
└── .database_connection
```

### Steps
1. Create the project structure:
   ```
   mkdir -p MyProject2/{Images,Code,Configs}
   touch MyProject2/Configs/.secret_key
   touch MyProject2/{.config,.database_connection}
   ```

2. Verify the structure (including hidden files):
   ```
   tree -a MyProject2
   ```

## Assignment 3: Simulate a Git-Initialized Project

### Objective
Mimic a programming project directory that uses Git for version control.

### Folder and File Structure
```
MyProject3/
│
├── Images/
│
├── Code/
│
├── Configs/
│
└── .git/
    ├── config
    ├── HEAD
    ├── description
    ├── hooks/
    ├── info/
    ├── objects/
    └── refs/
```

### Steps
1. Create the project structure:
   ```
   mkdir -p MyProject3/{Images,Code,Configs,.git/{hooks,info,objects,refs}}
   touch MyProject3/.git/{config,HEAD,description}
   ```

2. Verify the structure (including hidden files):
   ```
   tree -a MyProject3
   ```

## Conclusion

In this lab, you've practiced creating various file and directory structures, including hidden files and a simulated Git repository structure. These skills are fundamental for working with Linux systems and managing projects. Remember to use the `tree` command (with the `-a` flag for hidden files) to verify your structures. If `tree` is not available, the `find` command can be used as an alternative.

