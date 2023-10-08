import random
import datetime

# Define constants
LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]
MODULES = ["AUTH", "DATABASE", "NETWORK", "UI", "API"]
LOG_MESSAGES = {
    "INFO": ["User logged in.", "New entry added.", "Connection established.", "Session started."],
    "WARNING": ["Login retries almost exhausted.", "DB nearing max capacity.", "Network latency detected.", "UI unresponsive."],
    "ERROR": ["Failed login attempt.", "DB connection lost.", "Network error.", "UI crashed."],
    "DEBUG": ["Auth method called.", "DB query executed.", "Network packet sent.", "UI button clicked."]
}
LOG_FILE = "application.log"
NUM_OF_LOGS = 1000  # Number of log entries to generate

def generate_log():
    """
    Generate a single pseudo-log entry.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_level = random.choice(LOG_LEVELS)
    module = random.choice(MODULES)
    message = random.choice(LOG_MESSAGES[log_level])
    
    return f"[{timestamp}] [{log_level}] [{module}]: {message}"

def main():
    """
    Generate the pseudo-log file.
    """
    with open(LOG_FILE, "w") as log_file:
        for _ in range(NUM_OF_LOGS):
            log_file.write(generate_log() + "\n")
    print(f"{NUM_OF_LOGS} pseudo-log entries generated in {LOG_FILE}.")

if __name__ == "__main__":
    main()
