import os
import random

# Generate .py files
for i in range(5):
    with open(f"module_{i}.py", 'w') as f:
        f.write(f"def function_{i}():\n")
        if i % 2 == 0:
            f.write("    print('This is a print statement')\n")
        f.write("\n")
        f.write("# TODO: Check this function later\n")
        f.write("dbConnection = 'Some connection string here'\n")
        f.write(f"def another_function_{i}():\n")
        f.write("    pass\n")

# Generate app.log
log_levels = ["INFO", "DEBUG", "WARNING", "ERROR"]
urls = [
    "http://example.com/resource1",
    "https://secure-example.com/resource2",
    "http://another-example.com/page"
]

with open("app.log", 'w') as f:
    for i in range(20):
        random_log = random.choice(log_levels)
        if random_log == "ERROR":
            f.write(f"[ERROR] There was an error on module_{random.randint(0,4)}.py\n")
        elif random_log == "DEBUG":
            f.write(f"[DEBUG] Accessing {random.choice(urls)}\n")
        else:
            f.write(f"[{random_log}] This is a log statement\n")

print("Python files and app.log generated!")
