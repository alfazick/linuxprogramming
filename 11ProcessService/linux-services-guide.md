# Linux Services and Daemons: A Practical Guide

## Theoretical Framework

### Introduction to Linux Services
Linux services, also known as "daemons", are background processes that:
- Start at boot time
- Run continuously
- Operate without direct user interaction
- Provide core system functionalities

### Key Concepts
1. **Daemons**
   - Background services (web servers, databases, file servers)
   - Run automatically
   - Minimal user interaction

2. **Systemd**
   - Modern init system
   - Service manager
   - System process manager
   - Boot process manager

3. **Service Management**
   - Process control
   - Boot behavior
   - Status monitoring

4. **Service-Client Architecture**
   - Network accessibility
   - Remote connections
   - User permissions

## Core Commands Reference

### Systemctl Commands
```bash
# Basic service management
systemctl start [service_name]    # Start a service
systemctl stop [service_name]     # Stop a service
systemctl restart [service_name]  # Restart a service
systemctl status [service_name]   # Check service status
systemctl enable [service_name]   # Enable on boot
systemctl disable [service_name]  # Disable on boot
```

### Monitoring Commands
```bash
journalctl                # View systemd logs
ps aux | grep [service]  # View specific service process
netstat -tuln            # View network connections
ss -tuln                 # Modern replacement for netstat
```

## Practical Laboratory: MySQL Server Setup

### Lab 1: MySQL Server Installation and CRUD Operations

#### 1. Installation and Security Setup
```bash
# Update system
sudo apt update

# Install MySQL
sudo apt install mysql-server

# Secure the installation
sudo mysql_secure_installation

# Verify service status
systemctl status mysql.service
```

#### 2. MySQL Shell Access
```bash
# Access MySQL shell
sudo mysql -u root -p
```

#### 3. Database and Table Creation
```sql
-- Create database
CREATE DATABASE testdb;

-- Select database
USE testdb;

-- Create table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100)
);
```

#### 4. CRUD Operations Demo
```sql
-- Create: Insert data
INSERT INTO employees (name, position) VALUES ('John Doe', 'Software Engineer');
INSERT INTO employees (name, position) VALUES ('Jane Smith', 'Project Manager');

-- Read: Query data
SELECT * FROM employees;

-- Update: Modify data
UPDATE employees SET position = 'Senior Software Engineer' WHERE name = 'John Doe';

-- Delete: Remove data
DELETE FROM employees WHERE name = 'Jane Smith';
```

### Lab 2: Network Access Configuration

#### 1. User Creation and Permissions
```sql
-- Create new user
CREATE USER 'newuser'@'%' IDENTIFIED BY 'user_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON testdb.* TO 'newuser'@'%';

-- Apply changes
FLUSH PRIVILEGES;
```

#### 2. Remote Access Configuration
```bash
# Edit MySQL configuration
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

# Change bind-address to
bind-address = 0.0.0.0

# Restart service
sudo systemctl restart mysql.service
```

#### 3. Remote Client Setup
```bash
# On client machine
sudo apt update
sudo apt install mysql-client

# Get server IP (on server)
sudo apt install net-tools
ifconfig

# Connect from client
mysql -h server_ip -u newuser -p
```

## Cleanup and Security

### Database Cleanup
```sql
-- List databases
SHOW DATABASES;

-- Delete database
DROP DATABASE database_name;
```

### Complete MySQL Removal
```bash
# Stop service
sudo systemctl stop mysql

# Remove packages
sudo apt-get remove --purge mysql-server mysql-client mysql-common

# Clean dependencies
sudo apt-get autoremove

# Remove configuration files
sudo rm -rf /etc/mysql /var/lib/mysql
sudo apt-get purge mysql-server-core-* mysql-client-core-*

# Final cleanup
sudo apt-get autoremove
sudo apt-get autoclean

# Check for remaining processes
ps -A | grep mysql
```

## Security Best Practices

1. **User Management**
   - Create specific users for applications
   - Limit privileges to necessary databases
   - Avoid using root for remote connections

2. **Network Security**
   - Use specific IP addresses instead of 0.0.0.0
   - Configure firewall rules
   - Use SSL/TLS for connections

3. **Regular Maintenance**
   - Monitor logs regularly
   - Keep MySQL updated
   - Backup databases regularly

## Troubleshooting Tips

1. **Service Won't Start**
   - Check logs: `journalctl -u mysql.service`
   - Verify permissions: `ls -l /var/lib/mysql`
   - Check disk space: `df -h`

2. **Connection Issues**
   - Verify binding address
   - Check firewall rules
   - Test network connectivity

3. **Performance Problems**
   - Monitor resource usage
   - Check slow query log
   - Optimize configurations

