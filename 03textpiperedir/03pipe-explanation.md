# Understanding Pipes in Command Line

## Before Pipe

```mermaid
graph TD
    subgraph "Before Pipe"
        subgraph "Command 1"
            B1[Command 1]
            B1FD0[FD 0: stdin]
            B1FD1[FD 1: stdout]
            B1FD2[FD 2: stderr]
            B1 --- B1FD0
            B1 --- B1FD1
            B1 --- B1FD2
        end
        subgraph "Command 2"
            B2[Command 2]
            B2FD0[FD 0: stdin]
            B2FD1[FD 1: stdout]
            B2FD2[FD 2: stderr]
            B2 --- B2FD0
            B2 --- B2FD1
            B2 --- B2FD2
        end
    end
```

In this initial state, each command has its own standard input (stdin), standard output (stdout), and standard error (stderr) streams. These are typically connected to the terminal or other default sources/destinations.

## After Pipe: Command 1 | Command 2

```mermaid
graph TD
    subgraph "After Pipe: Command 1 | Command 2"
        A1[Command 1]
        A2[Command 2]
        A1FD0[FD 0: stdin]
        A1FD1[FD 1: pipe write]
        A1FD2[FD 2: stderr]
        A2FD0[FD 0: pipe read]
        A2FD1[FD 1: stdout]
        A2FD2[FD 2: stderr]
        PIPE((Pipe))
        A1 --- A1FD0
        A1 --- A1FD1
        A1 --- A1FD2
        A2 --- A2FD0
        A2 --- A2FD1
        A2 --- A2FD2
        A1FD1 --> PIPE
        PIPE --> A2FD0
    end
```

When a pipe is used:

1. Command 1's stdout (FD 1) is connected to the write end of the pipe.
2. Command 2's stdin (FD 0) is connected to the read end of the pipe.
3. This allows the output of Command 1 to be directly fed as input to Command 2.
4. stderr (FD 2) for both commands typically remains connected to the terminal.
5. Command 1's stdin and Command 2's stdout also typically remain connected to the terminal.

The pipe acts as a buffer, allowing data to flow from Command 1 to Command 2 without needing to be stored in a temporary file or displayed on the screen.
