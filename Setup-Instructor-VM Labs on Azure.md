
# Azure Lab Services Setup Guide

This guide outlines the process to set up Azure Lab Services with Linux VMs.

## Prerequisites

- **Azure Subscription**: If you don't have one, [sign up for Azure](https://azure.com/free).

## Steps

### 1. Create a Lab Plan

- Navigate to the Azure portal.
- Click on **Create a resource**.
- Search for "Lab Services" and select **Lab Plan**.
- Click **Create**.
- Fill out the necessary fields: Subscription, Resource Group, and a name for the Lab Plan.

### 2. Create a Lab Account

- Within the created Lab Plan, select **+ Add**.
- Provide a name for the Lab Account and fill in any other required details.

### 3. Create a Lab

- Inside the Lab Account, find and select the option to create a new lab.
- Define the VM type, software configurations, and other specifics for this lab.

### 4. Template VM Configuration

- Start the template VM from within the lab.
- Once active, connect to the VM. For Linux VMs, use SSH.
- Install and configure any required software or tools.
- After setting up, shut down the VM.

### 5. Publish the Lab

- In the lab settings, choose **Publish**.
- Define the number of VM instances and the level of user access.
- Share the registration link with users for them to access the VMs.

### 6. Accessing the Lab VMs

- Users can register using the provided link.
- After registration, they can start, stop, and connect to the VMs as per the permissions you've set.

### 7. Monitoring and Management

- Monitor VM usage, active VMs, and user activity.
- Adjust user access, start/stop VMs, or reset environments as necessary.

### 8. Clean-Up

- Delete labs or Lab Plans that are no longer required to prevent unnecessary charges.

## Notes

Always refer to the [official Azure documentation](https://docs.microsoft.com/azure) for the most updated processes and best practices.

