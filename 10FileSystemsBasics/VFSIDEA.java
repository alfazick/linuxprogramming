// Defining a "VFS" interface with abstract methods resembling file operations
interface VFS {
    void read(String fileName);
    void write(String fileName, String data);
    void open(String fileName);
    void close(String fileName);
}

// An "Ext4" class implementing the VFS interface and providing concrete implementations for the operations
class Ext4 implements VFS {
    @Override
    public void read(String fileName) {
        System.out.println("Ext4 reading file: " + fileName);
    }

    @Override
    public void write(String fileName, String data) {
        System.out.println("Ext4 writing data to file: " + fileName);
    }

    @Override
    public void open(String fileName) {
        System.out.println("Ext4 opening file: " + fileName);
    }

    @Override
    public void close(String fileName) {
        System.out.println("Ext4 closing file: " + fileName);
    }
}

// An "XFS" class implementing the VFS interface, with its own concrete implementations for the operations
class XFS implements VFS {
    @Override
    public void read(String fileName) {
        System.out.println("XFS reading file: " + fileName);
    }

    @Override
    public void write(String fileName, String data) {
        System.out.println("XFS writing data to file: " + fileName);
    }

    @Override
    public void open(String fileName) {
        System.out.println("XFS opening file: " + fileName);
    }

    @Override
    public void close(String fileName) {
        System.out.println("XFS closing file: " + fileName);
    }
}

// A test class to demonstrate the concept
public class VFSIDEA {
    public static void main(String[] args) {
        VFS ext4 = new Ext4();
        ext4.open("document.txt");
        ext4.read("document.txt");
        ext4.write("document.txt", "Hello, World!");
        ext4.close("document.txt");
        
        VFS xfs = new XFS();
        xfs.open("document.txt");
        xfs.read("document.txt");
        xfs.write("document.txt", "Hello, World!");
        xfs.close("document.txt");
    }
}
