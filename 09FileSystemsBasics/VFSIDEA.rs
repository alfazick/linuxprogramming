// Defining a trait to represent the VFS interface
trait VFS {
    fn read(&self, file_name: &str);
    fn write(&self, file_name: &str, data: &str);
    fn open(&self, file_name: &str);
    fn close(&self, file_name: &str);
}

// Implementing the VFS trait for a hypothetical Ext4 file system
struct Ext4;

impl VFS for Ext4 {
    fn read(&self, file_name: &str) {
        println!("Ext4 reading file: {}", file_name);
    }

    fn write(&self, file_name: &str, data: &str) {
        println!("Ext4 writing data to file: {}", file_name);
    }

    fn open(&self, file_name: &str) {
        println!("Ext4 opening file: {}", file_name);
    }

    fn close(&self, file_name: &str) {
        println!("Ext4 closing file: {}", file_name);
    }
}

// Implementing the VFS trait for a hypothetical XFS file system
struct XFS;

impl VFS for XFS {
    fn read(&self, file_name: &str) {
        println!("XFS reading file: {}", file_name);
    }

    fn write(&self, file_name: &str, data: &str) {
        println!("XFS writing data to file: {}", file_name);
    }

    fn open(&self, file_name: &str) {
        println!("XFS opening file: {}", file_name);
    }

    fn close(&self, file_name: &str) {
        println!("XFS closing file: {}", file_name);
    }
}

fn main() {
    let ext4 = Ext4;
    ext4.open("document.txt");
    ext4.read("document.txt");
    ext4.write("document.txt", "Hello, World!");
    ext4.close("document.txt");
    
    let xfs = XFS;
    xfs.open("document.txt");
    xfs.read("document.txt");
    xfs.write("document.txt", "Hello, World!");
    xfs.close("document.txt");
}
