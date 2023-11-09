# cpu_load_simulator.py
import threading
import time
import tempfile
import syslog

# Function to simulate CPU intensive task
def cpu_intensive_task():
    while True:
        # Perform a calculation that uses CPU resources
        [x**2 for x in range(10000)]

# Create and start multiple threads to increase CPU load
def create_load(threads=4):
    syslog.syslog(syslog.LOG_INFO, f"Simulating high CPU load with {threads} threads.")
    for _ in range(threads):
        thread = threading.Thread(target=cpu_intensive_task)
        thread.daemon = True  # allows thread to exit when main thread exits
        thread.start()

# Run the function to create CPU load
if __name__ == "__main__":
    try:
        # You can change the number of threads to increase or decrease the load
        create_load(threads=8)

        # Demonstrate creating a temporary file
        with tempfile.NamedTemporaryFile() as temp_file:
            syslog.syslog(syslog.LOG_INFO, f"Created temporary file at {temp_file.name}")
            # Keep the program running
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        syslog.syslog(syslog.LOG_INFO, "Load simulation stopped by user.")
