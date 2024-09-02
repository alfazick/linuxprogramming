# Linux Navigation Commands Tutorial

This tutorial focuses on essential commands for navigating the Linux filesystem.

## 1. pwd: Print Working Directory

The `pwd` command shows the full path of the current working directory.

```bash
pwd
```

Example output:
```
/home/username/documents
```

## 2. ls: List Directory Contents

The `ls` command lists files and directories in the current directory.

Basic usage:
```bash
ls
```

Useful options:
- `ls -l`: Long format, showing permissions, owner, size, and modification date
- `ls -a`: Shows hidden files (those starting with a dot)
- `ls -h`: Human-readable file sizes
- `ls -R`: Recursively list subdirectories

Examples:
```bash
ls -l
ls -la
ls -lh /etc
```

## 3. cd: Change Directory

The `cd` command is used to change the current working directory.

Basic usage:
```bash
cd directory_name
```

Special uses:
- `cd` or `cd ~`: Change to home directory
- `cd ..`: Move up one directory
- `cd -`: Switch to the previous directory
- `cd /`: Change to root directory

Examples:
```bash
cd /etc
cd ~/documents
cd ../../
```

## 4. tree: Display Directory Structure

While not always pre-installed, `tree` is excellent for visualizing directory structures.

Basic usage:
```bash
tree
```

Useful options:
- `tree -L n`: Limit display to n levels deep
- `tree -d`: Show only directories

Example:
```bash
tree -L 2 /etc
```

## 5. find: Search for Files and Directories

The `find` command can be used for navigation by locating files and directories.

Basic usage:
```bash
find /path/to/search -name "filename"
```

Example:
```bash
find /home/username -name "*.txt"
```

## 6. which: Locate a Command

The `which` command shows the full path of shell commands.

Basic usage:
```bash
which command_name
```

Example:
```bash
which python
```

## Navigation Tips

1. Use Tab for auto-completion of file and directory names.
2. Use wildcards (`*`, `?`) with `ls` and `find` for flexible searching.
3. The `/` at the beginning of a path indicates the root directory.
4. `~` is a shortcut for your home directory.
5. Use relative paths (without leading `/`) for locations relative to your current directory.

## Practice Exercises

1. Starting from your home directory, navigate to `/etc`, list its contents, then return to your home directory.
2. Create a directory structure in your home folder: `~/test/subdir1/subdir2`. Navigate into `subdir2` using a single command.
3. Use `find` to locate all `.conf` files in the `/etc` directory.
4. Use `tree` to display the structure of your home directory, limiting the output to 2 levels deep.

Remember, practice is key to becoming comfortable with these navigation commands. Experiment in a safe directory to gain confidence in moving around the Linux filesystem.
