# file_wait.py
with open('/tmp/testfile.txt', 'w') as f:
    print("File is open. Please enter any text and press enter:")
    user_input = input()
    f.write(user_input)
    print("You've written to the file!")
