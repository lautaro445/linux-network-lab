# Firewall Configuration

## Overview

In this lab, the goal was to set up a basic firewall on the server VM to prevent undesired network communication while allowing essential services. The firewall configuration was intentionally kept minimal, serving as a foundation for future, more restrictive rules. No conflicts with the DHCP service were encountered.

### Tools Used

- **UFW** (Uncomplicated Firewall)  
- **iptables**  

---

## Configuration

- Allowed **DNS traffic** (port 53) to enable name resolution.  
- Other ports were left in their default state, as they were already in use and correctly configured.  
- No additional restrictions were applied at this stage.

**Example commands used:**

```bash
# Enable UFW
sudo ufw enable

# Allow DNS traffic
sudo ufw allow 53

# Check UFW status and rules
sudo ufw status verbose

# List iptables rules
sudo iptables -L -v -n
Note: These commands are examples; the main goal was to create a basic working firewall without interfering with DHCP or other services.

#Verification

Confirmed that port 53 (DNS) was allowed.

Verified that existing services continued to operate without interruption.

Ensured no conflicts with DHCP or other network communication.
