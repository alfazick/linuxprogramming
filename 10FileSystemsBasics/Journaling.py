class JournalingFileSystem:
    def __init__(self):
        self.file_system = {}
        self.journal = []

    def write(self, filename, data):
        # Log the operation in the journal
        self.journal.append(("write", filename, data))
        # Modify the file system immediately
        self.file_system[filename] = data

    def delete(self, filename):
        # Log the operation in the journal but do not modify the file system immediately
        self.journal.append(("delete", filename))

    def crash_recovery(self):
        # Clear the current state of the file system
        self.file_system = {}
        # Replay the journal to restore the file system to the last consistent state
        for operation, filename, *args in self.journal:
            if operation == "write":
                self.file_system[filename] = args[0]
            elif operation == "delete":
                self.file_system.pop(filename, None)
        
    def display(self):
        print(f"File System: {self.file_system}")
        print(f"Journal: {self.journal}")


# Example usage
fs = JournalingFileSystem()
fs.write("file1.txt", "Hello, World!")
fs.write("file2.txt", "Hello, Journaling!")
fs.delete("file1.txt")
fs.display()

print("\nSimulating crash...\n")
fs.crash_recovery()
fs.display()
