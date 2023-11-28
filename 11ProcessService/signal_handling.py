
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