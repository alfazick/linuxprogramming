# Lab: Adding a User to Sudoers List

## Objective
Learn how to create a new user, add them to the sudoers list, verify their sudo privileges, and properly clean up afterwards in a standard Ubuntu environment.


## Lab Steps

### 1. Create a New User
```bash
sudo useradd -m newuser
```
This creates a new user 'newuser' with a home directory.

### 2. Set Password for New User
```bash
sudo passwd newuser
```
Set a password for the new user when prompted.

### 3. Verify User Creation
```bash
id newuser
ls -l /home/newuser
```
This should display the user's UID, GID, groups, and confirm the existence of their home directory.

### 4. Add User to sudo Group
```bash
sudo usermod -aG sudo newuser
```

### 5. Verify Group Membership
```bash
groups newuser
```
You should see 'sudo' listed among the groups.

### 6. Check sudoers File
```bash
sudo visudo
```
Look for this line, which grants sudo privileges to members of the sudo group:
```
%sudo   ALL=(ALL:ALL) ALL
```

### 7. Test sudo Access
Switch to the new user:
```bash
su - newuser
```
Try running a command with sudo:
```bash
sudo ls /root
```
You should be prompted for newuser's password, then see the contents of /root.

### 8. Verify sudo Privileges
```bash
sudo -l
```
This will show the sudo privileges for the current user (newuser).

### 9. Exit newuser Session
```bash
exit
```
This will return you to your original user session.

### 10. Cleanup
Remove the test user and their home directory:
```bash
sudo userdel -r newuser
```

### 11. Verify Cleanup
Confirm that the user has been removed:
```bash
id newuser
ls -l /home/newuser
```
Both commands should return errors, indicating that the user and their home directory no longer exist.

## Conclusion
You've successfully:
1. Created a new user
2. Added them to the sudo group
3. Verified their sudo privileges
4. Properly cleaned up by removing the test user

This process demonstrates the full lifecycle of adding and removing a user with sudo privileges. It's crucial to always clean up after such operations, especially in production or shared environments, to maintain system security and hygiene.
