# Python Network Test Script

## Overview

This Python script was developed to automate basic network connectivity and SSH access testing. It allows the user to verify if a target IP is reachable, check the status of port 22 (SSH), and attempt an SSH connection to ensure the host is accessible and ready for remote login.

---

## Functionality

The script performs the following tasks:

1. **Ping Test:**  
   - Requests an IP address from the user.  
   - Sends a ping to the specified IP.  
   - If the host is unreachable, it notifies the user.

2. **Port 22 Check:**  
   - Verifies if port 22 (SSH) is open.  
   - If the port is closed, it prompts the user to optionally change the port for testing.

3. **SSH Connection Test:**  
   - Requests a username and password from the user.  
   - Attempts to log in via SSH to the target host.  
   - Reports success or failure, confirming connectivity and SSH access.

---

## Dependencies

- Python 3.x  
- Standard libraries: `os`, `subprocess`, `socket`  
- Optional: `paramiko` if using SSH connections (common for Python SSH automation)

---

## Usage

Run the script using Python 3:

```bash
python3 network_test.py

#Follow the prompts:

Enter the target IP.

Wait for the ping result.

Check port 22 status and optionally change it if closed.

Enter SSH credentials to test login.

The script outputs messages to the console indicating the success or failure of each step.

#Verification

Successfully pinged the target IP.

Confirmed port 22 is open.

SSH login test either succeeded or provided a clear failure message.

Demonstrates automated verification of connectivity and remote access.

