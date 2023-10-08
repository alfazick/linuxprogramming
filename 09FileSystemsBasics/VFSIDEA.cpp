#include <iostream>
#include <string>

// Abstract class to represent the VFS interface
class Interface {
public:
    virtual void read(const std::string& fileName) = 0;
    virtual void write(const std::string& fileName, const std::string& data) = 0;
    virtual void open(const std::string& fileName) = 0;
    virtual void close(const std::string& fileName) = 0;

    virtual ~Interface() = default;
};

// Struct to represent the superblock data, including maximum file and volume size
struct Superblock {
    uint64_t maxFileSize;
    uint64_t maxVolumeSize;
};

// Ext4 class implementing the VFS interface and providing concrete implementations for the operations
class Ext4 : public Interface {
public:
    Ext4(Superblock sb, const std::string& ds) : superblock(sb), dataStructures(ds) {}

    void read(const std::string& fileName) override {
        std::cout << "Ext4 reading file: " << fileName << '\n';
    }

    void write(const std::string& fileName, const std::string& data) override {
        std::cout << "Ext4 writing data to file: " << fileName << '\n';
    }

    void open(const std::string& fileName) override {
        std::cout << "Ext4 opening file: " << fileName << '\n';
    }

    void close(const std::string& fileName) override {
        std::cout << "Ext4 closing file: " << fileName << '\n';
    }

private:
    Superblock superblock;
    std::string dataStructures;
};

// XFS class implementing the VFS interface and providing concrete implementations for the operations
class XFS : public Interface {
public:
    XFS(Superblock sb, const std::string& ds) : superblock(sb), dataStructures(ds) {}

    void read(const std::string& fileName) override {
        std::cout << "XFS reading file: " << fileName << '\n';
    }

    void write(const std::string& fileName, const std::string& data) override {
        std::cout << "XFS writing data to file: " << fileName << '\n';
    }

    void open(const std::string& fileName) override {
        std::cout << "XFS opening file: " << fileName << '\n';
    }

    void close(const std::string& fileName) override {
        std::cout << "XFS closing file: " << fileName << '\n';
    }

private:
    Superblock superblock;
    std::string dataStructures;
};

int main() {
    uint64_t default_size = 16 * 1024;
    Superblock ext4SB {default_size,default_size};
    Ext4 ext4(ext4SB, "HTree");
    
    Superblock xfsSB {default_size, default_size};
    XFS xfs(xfsSB, "B+Tree");

    ext4.open("document.txt");
    ext4.read("document.txt");
    ext4.write("document.txt", "Hello, World!");
    ext4.close("document.txt");
    
    xfs.open("document.txt");
    xfs.read("document.txt");
    xfs.write("document.txt", "Hello, C++!");
    xfs.close("document.txt");

    return 0;
}
