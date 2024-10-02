# File Descriptors vs. Inode Numbers

File descriptors and inode numbers are different concepts that pertain to different layers in a filesystem's architecture. Let's delve into each term individually to differentiate them properly:

## Inode Number

### Definition
An inode (index node) is a data structure on a filesystem on Unix and Linux systems which stores information about a file or directory, including attributes (like permissions, ownership) and disk block locations which essentially define the file or directory.

### Characteristics
- **Uniqueness**: Every file or directory has a unique inode number within the filesystem.
- **Persistence**: Inode information is persistent across reboots; it resides on the disk until the file is deleted.
- **Usage**: It is used by the filesystem to manage files and directories.

## File Descriptor

### Definition
A file descriptor is an abstract indicator used by the kernel to access a file or other input/output resource, such as a pipe or network socket. It is typically an integer that is used to identify an open file within a process.

### Characteristics
- **Uniqueness**: File descriptors are unique per process. Different processes can have file descriptors with the same number, but within a process, each open file has a unique descriptor.
- **Persistence**: File descriptors are not persistent across reboots, and they cease to exist when a process terminates.
- **Usage**: File descriptors are used by processes to read from or write to open files through system calls like `read()` and `write()`.

## Example

A file named "example.txt" will have an inode number that contains metadata information about the file. This inode number is unique on the filesystem and can be used to identify the file at the filesystem level.

When a process opens "example.txt" to read or write, the kernel assigns a file descriptor to this open file in the context of the process. This file descriptor is used by the process to perform operations on the open file.

## Summary

- **File descriptor**: Process-specific and used to refer to an open file during the runtime of a process.
- **Inode number**: Filesystem-specific and used to refer to a file or directory persistently within the filesystem, irrespective of whether any process has the file open.
