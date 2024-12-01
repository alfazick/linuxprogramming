# Processes 101: Comprehensive Guide on Linux Process Management

## Theoretical Framework

### Introduction: The Essence of Processes in Linux
Processes in Linux are instances of executing programs, critical in multitasking and multi-user environments.

### Process States: Understanding the Lifecycle
- Running: Executing or ready to execute
- Waiting: Interruptible and Uninterruptible states
- Stopped: Halted, can be restarted
- Zombie: Finished, waiting for parent to read exit status

### Process Hierarchy and Identification
Parent and child processes each have unique Process IDs (PIDs) and Parent Process IDs (PPIDs).

### Advanced Process Management Commands
- ps: Explores active processes
- top: Real-time system monitoring
- kill: Signal-based process management

### Daemon Processes: The Silent Workers
Daemon processes run in the background, performing critical system tasks.

### Managing Foreground and Background Processes
Strategies for toggling between foreground and background using bg, fg, and &.

### Process Priority: Nice and Renice
Adjusting process priority using nice and renice for resource allocation.

## Reference Tables

### Table 1: Process States in Linux
| State | Description |
|-------|-------------|
| Running | Executing or ready to execute |
| Waiting (Interruptible) | Waiting for event/resource |
| Waiting (Uninterruptible) | Waiting, not interruptible |
| Stopped | Halted, can be restarted |
| Zombie | Finished, waiting for parent |

### Table 2: Common Linux Signals
| Signal Number | Signal Name | Description |
|--------------|-------------|-------------|
| 1 | SIGHUP | Hangup detected, reload |
| 2 | SIGINT | Interrupt from keyboard |
| 9 | SIGKILL | Force terminate |
| 15 | SIGTERM | Graceful termination |
| 17, 19, 23 | SIGSTOP | Stop process |
| 18, 20, 24 | SIGCONT | Continue if stopped |

## Practical Laboratory Guide

### Lab Preparation
Prerequisites:
- Linux environment
- Python 3
- Text editor (nano or vim)

### Lab Exercise 1: Process States
```python
# input_wait.py
input("Press Enter to continue...")
```

#### Demonstration and Solution
```bash
# Terminal 1
$ python3 input_wait.py
Press Enter to continue...  # Process waits here

# Terminal 2 - Observe process state
$ ps aux | grep input_wait.py
user     12345  0.0  0.1  23456  1234 pts/0    S+   10:00   0:00 python3 input_wait.py
```

### Lab Exercise 2: Continuous Process
```python
# infinite_loop.py
import time
i = 1
while True:
    print(i)
    i += 1
    time.sleep(1)
```

#### Demonstration and Solution
```bash
# Start process
$ python3 infinite_loop.py
1
2
3...

# Process Control
Ctrl+Z  # Suspend
$ bg    # Continue in background
$ fg    # Bring to foreground
```

### Lab Exercise 3: Signal Handling
```python
# signal_handling.py
import signal
import time

def signal_handler(signum, frame):
    print("SIGTERM received, but not terminating")

signal.signal(signal.SIGTERM, signal_handler)

print("Running... (try to send SIGTERM)")
while True:
    time.sleep(1)
```

#### Demonstration and Solution
```bash
# Terminal 1
$ python3 signal_handling.py
Running... (try to send SIGTERM)

# Terminal 2
$ pid=$(pgrep -f signal_handling.py)
$ kill -SIGTERM $pid
# Terminal 1 shows: SIGTERM received, but not terminating
```

### Lab Exercise 4: Process Creation
```python
# process_creation.py
import os
import time

pid = os.fork()

if pid > 0:
    print(f"Parent process (PID: {os.getpid()}), Child PID: {pid}")
    os.wait()
else:
    print(f"Child process (PID: {os.getpid()}) running")
    time.sleep(100)
    print("Child process finishing")

print("Process (PID: {}) completed".format(os.getpid()))
```

#### Demonstration and Solution
```bash
$ python3 process_creation.py
Parent process (PID: 12347), Child PID: 12348
Child process (PID: 12348) running

# Verify hierarchy
$ pstree -p 12347
python3(12347)───python3(12348)
```

### Process Priority Experiments using Fibonacci

```python
# fibonacci.py
import sys
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fibonacci.py [n]")
        sys.exit(1)

    n = int(sys.argv[1])
    print(f"Calculating Fibonacci({n})")
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f"Result: {result}")
    print(f"Execution Time: {end_time - start_time} seconds")
```

#### Priority Management Demonstrations
1. Default Priority:
```bash
$ python3 fibonacci.py 35
```

2. Modified Priority:
```bash
$ nice -n 10 python3 fibonacci.py 35
```

3. Dynamic Priority:
```bash
$ python3 fibonacci.py 35 &
$ renice -n 10 -p $!
```

## Verification and Troubleshooting

### Process State Verification
```bash
# View process status
$ ps -o pid,ppid,state,cmd -p [PID]

# Monitor resources
$ top -p [PID]
```

### Common Issues and Solutions
1. Permission Denied:
```bash
# Solution: Use sudo for negative nice values
$ sudo nice -n -20 python3 fibonacci.py 35
```

2. Process Not Found:
```bash
# Solution: Verify PID first
$ ps aux | grep process_name
```

## Important Notes
1. Check signal numbers with `kill -l`
2. SIGSTOP and SIGKILL cannot be caught/ignored
3. Use signals carefully with system processes
4. Only root can set negative nice values
5. Monitor system impact when adjusting priorities

## Observations and Analysis
- Document execution times under different nice values
- Note impact of priority changes
- Observe process behavior with different signals
- Track parent-child process relationships

## Conclusion
This guide provides a comprehensive view of process behavior and control in Linux through practical exercises and demonstrations. The combination of theoretical knowledge and hands-on practice helps develop a deep understanding of Linux process management.
