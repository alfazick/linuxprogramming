

# File abstraction, what is relevant only inode object

class File:
    def __init__(self, name, inode):
        self.name = name
        self.inode = inode

    def read(self):
        data_blocks = self.inode.data_block_pointers
        content = ""
        for block_number in data_blocks:
            content += f"Data Block {block_number}: {disk_space[block_number]}\n"
        return content

    def write(self, data):
        pass  # In this abstraction, writing to the file is not implemented.




# Defining the inode class which will store metadata about each file
# An inode object with pointers to data blocks where the file's content is stored
class Inode:
    def __init__(self, inode_number, file_type, permissions, size, data_block_pointers):
        self.inode_number = inode_number
        self.file_type = file_type
        self.permissions = permissions
        self.size = size
        self.data_block_pointers = data_block_pointers
        self.timestamps = {'creation': None, 'modification': None}



# Defining the dentry class to map file names to inodes and store in a cache
class Dentry:
    def __init__(self):
        self.dentry_cache = {}

    def add_dentry(self, file_name, file):
        self.dentry_cache[file_name] = file

    def lookup_dentry(self, file_name):
        return self.dentry_cache.get(file_name)



# Data blocks on the "disk" (for demonstration purposes)
disk_space = {
    1: "Data block 1: The actual content of the file (part 1)...",
    2: "Data block 2: The actual content of the file (part 2)...",
    3: "Data block 3: The actual content of the file (part 3)...",
    4: "",  # Empty data block for directories or unused blocks
    5: "",
    6: "",
}

# Creating a few Inode objects to represent different files and directories in our filesystem
inode1 = Inode(inode_number=1, file_type='regular file', permissions='rw-r--r--', size=1024, data_block_pointers=[1, 2, 3])
inode2 = Inode(inode_number=2, file_type='directory', permissions='rwxr-xr-x', size=4096, data_block_pointers=[4, 5, 6])

# Creating File and Directory objects that associate with specific Inodes
file1 = File(name='file1.txt', inode=inode1)
directory1 = File(name='my_directory', inode=inode2)

# Adding entries to the dentry cache, associating file and directory names with File objects
dentry_cache = Dentry()
dentry_cache.add_dentry(file1.name, file1)
dentry_cache.add_dentry(directory1.name, directory1)

# Demonstrating a lookup in the dentry cache to find a file or directory based on its name
name_to_lookup = 'file1.txt'
found_entry = dentry_cache.lookup_dentry(name_to_lookup)

if found_entry:
    if found_entry.inode.file_type == 'regular file':
        print(f"File '{name_to_lookup}' found with the following details:")
        print(f"  - Name: {found_entry.name}")
        print(f"  - Inode number: {found_entry.inode.inode_number}")
        print(f"  - File type: {found_entry.inode.file_type}")
        print(f"  - Permissions: {found_entry.inode.permissions}")
        print(f"  - Size: {found_entry.inode.size} bytes")
        print(f"  - Content:\n{found_entry.read()}")
    elif found_entry.inode.file_type == 'directory':
        print(f"Directory '{name_to_lookup}' found with the following details:")
        print(f"  - Name: {found_entry.name}")
        print(f"  - Inode number: {found_entry.inode.inode_number}")
        print(f"  - File type: {found_entry.inode.file_type}")
        print(f"  - Permissions: {found_entry.inode.permissions}")
else:
    print(f"Entry '{name_to_lookup}' not found in the file system.")
