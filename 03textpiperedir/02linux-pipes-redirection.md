# Idea of Pipes and Redirection

Time to awaken Sharingan :)

## Introduction

Ok I believe at this time you can start to feel boring, It's time to introduce mechanism which brings power. Namely Pipes and Redirection.

Most of the useful things you can accomplish in Linux, one way or another most likely involve one of these patterns. Pipes and redirection are fundamental concepts in Unix and Unix-like operating systems, and they're representative of the OS's philosophy of "everything is a file." 

## a) Pipes (|)

A pipe, symbolized as |, is a mechanism for inter-process communication. It allows the output of one process to be used as the input of another.

### Operating System Perspective

- Pipes are an example of a mechanism for Inter-Process Communication (IPC). 
- A pipe creates a linear communication channel between processes, often termed as a "half-duplex" channel, because data flows only in one direction. 
- Data written by the sending process can be read by the receiving process. 
- This is usually done in a buffered manner, which means data is stored in a temporary area (buffer) before it's sent to the receiving process.

### Practical Example

If you want to search for a specific word in a file and then count its occurrences, you might use grep to find the word and wc to count its occurrences, combined with a pipe:

```bash
cat filename.txt | grep "specific-word" | wc -l
```

Here:
1. `cat` outputs the content of the file. 
2. `grep` takes this output to find lines containing "specific-word" 
3. `wc` counts these lines.

## b) Redirection (>, >>, <)

Redirection allows you to direct the input and output streams of a process to a file or from a file.

### Operating System Perspective

The OS assigns every process a table of file descriptors. The first three are standard:
- 0: standard input (stdin)
- 1: standard output (stdout)
- 2: standard error (stderr)

Redirection works by changing the file descriptor table of a process. Instead of pointing to the default locations (e.g., the terminal), they're changed to point to a file.

### Examples

1. Output Redirection (> and >>):
   - `>`: Redirects the output of a command to a file. If the file exists, it's overwritten. If it doesn't, it's created.
     ```bash
     echo "Hello, World!" > output.txt
     ```
   - `>>`: Appends the output of a command to a file. If the file doesn't exist, it's created.
     ```bash
     echo "Hello again!" >> output.txt
     ```

2. Input Redirection (<):
   - Directs the input for a process from a file instead of from the standard input (typically the keyboard).
     ```bash
     sort < input.txt
     ```
   Here, `sort` reads its input from input.txt rather than the terminal.

## Conclusion

This model allows small utilities to be combined, enhancing the power and flexibility of the Linux command line.
