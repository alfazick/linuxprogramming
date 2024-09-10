import os
import random

def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Created: {filename}")

def create_content_files():
    # Create hello.txt
    create_file("hello.txt", "Hello, World!\nWelcome to Linux text manipulation.")

    # Create names.txt
    names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    create_file("names.txt", "\n".join(random.sample(names, len(names))))

    # Create numbers.txt
    numbers = [str(random.randint(1, 100)) for _ in range(20)]
    create_file("numbers.txt", "\n".join(numbers))

    # Create logfile.txt
    log_entries = [
        "2023-09-10 10:15:32 INFO: Application started",
        "2023-09-10 10:16:45 WARNING: Low memory warning",
        "2023-09-10 10:17:30 ERROR: Failed to connect to database",
        "2023-09-10 10:18:22 INFO: User logged in",
        "2023-09-10 10:19:15 DEBUG: Processing item 1",
        "2023-09-10 10:20:05 ERROR: Invalid input received",
        "2023-09-10 10:21:18 WARNING: CPU usage high",
        "2023-09-10 10:22:30 INFO: Task completed successfully",
        "2023-09-10 10:23:45 DEBUG: Closing connection",
        "2023-09-10 10:24:50 INFO: Application shutdown"
    ]
    create_file("logfile.txt", "\n".join(log_entries))

    # Create todo.txt
    todos = [
        "TODO: Implement new feature",
        "Buy groceries",
        "TODO: Fix bug in login system",
        "Call dentist for appointment",
        "TODO: Update documentation",
        "Prepare presentation for meeting",
        "TODO: Optimize database queries",
        "Plan weekend trip",
        "TODO: Write unit tests",
        "Send birthday card to mom"
    ]
    create_file("todo.txt", "\n".join(todos))

def main():
    # Create content files
    create_content_files()

if __name__ == "__main__":
    main()