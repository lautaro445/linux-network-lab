# DHCP Configuration

## Overview

In this lab, the goal was to configure a DHCP server on a KVM host to automatically assign IP addresses to the client VM. This allowed dynamic IP management in a controlled, isolated network environment. Challenges included initial misconfigurations, interference from KVM’s default NAT DHCP, and occasional duplicate IP assignments.

### Lab Topology
[Client VM] --- [KVM Host DHCP Server: 192.168.100.2]

- **Host OS:** Xubuntu (KVM hypervisor)
- **Server VM:** DHCP server, IP 192.168.100.2
- **Client VM:** Receives IP dynamically in the range 192.168.100.50–192.168.100.100
- **Network:** Isolated network `lab-local` created to prevent conflicts with KVM NAT DHCP

---

## Network Setup

- **Server IP:** `192.168.100.2`  
- **DHCP range:** `192.168.100.50` to `192.168.100.100`  
- **Isolated network:** `lab-local`  
- **Purpose:** Ensure the DHCP server is the only source of IP assignment within this network.

---

## Files and Configuration

### DHCP Configuration File

**Path:** `/etc/dhcp/dhcpd.conf`  

```text
# The ddns-updates-style parameter controls whether or not the server will
# attempt to do a DNS update when a lease is confirmed.
ddns-update-style none;

# If this DHCP server is the official DHCP server for the local network,
# the authoritative directive should be uncommented.
#authoritative;

subnet 192.168.100.0 netmask 255.255.255.0 {
    range 192.168.100.50 192.168.100.100;
    option routers 192.168.100.2;
    option domain-name-servers 8.8.8.8, 8.8.4.4;
}

DHCP Server Defaults
# On what interfaces should the DHCP server serve DHCP requests
INTERFACESv4="enp8s0"
INTERFACESv6=""

#Errors Encountered and Solutions

Server restart errors: Initially, restarting the DHCP service failed due to misconfiguration in dhcpd.conf.

Solution: Corrected the subnet, gateway, and DHCP range.

Interference from KVM NAT DHCP: The default NAT network provided IPs, conflicting with our server.

Solution: Created an isolated network lab-local to ensure the server controlled DHCP assignments.

Duplicate IPs: Sometimes, after restarting the server, the client received two IPs.

Solution: Reconfigured the DHCP file and restarted the service to ensure correct single IP assignment.

#Verification

Client VM successfully received IPs from the DHCP server within the range 192.168.100.50–100.

#Network connectivity verified using:
ip addr show
ip route
ping 192.168.100.2

#DHCP server service verified with:
sudo systemctl restart isc-dhcp-server
systemctl status isc-dhcp-server

