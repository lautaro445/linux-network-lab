<<<<<<< HEAD
# Linux Network Lab

Hands-on Linux networking and system administration lab built using Debian minimal virtual machines on KVM.

## Overview
This project simulates a small client-server environment designed to practice real-world Linux system administration, networking, and basic automation.

The lab was created as a personal learning project focused on understanding how core network services interact at a low level.

## Technologies Used
- Debian GNU/Linux (minimal installations)
- KVM / libvirt
- SSH
- DHCP (isc-dhcp-server)
- DNS (BIND9)
- iptables
- Python (automation)

## Lab Topology
- Host OS: Xubuntu
- Server VM: Debian minimal
- Client VM: Debian minimal
- Network type: Isolated virtual network (lab-local)

## Implemented Features
- Manual static IP configuration
- SSH access with key-based authentication
- Custom SSH port configuration
- DHCP server configuration
- Internal DNS with forward and reverse zones
- Basic firewall rules using iptables
- Python script for connectivity and SSH checks

## Current Status
- Internal DNS resolution working correctly
- Reverse DNS resolution working
- Client does not currently resolve external domains (Internet access pending)

## Planned Improvements
- Enable Internet access through forwarding/NAT
- DNS forwarding for external domains
- Add additional client VMs
- Improve automation scripts
- Service monitoring and logging

=======
# linux-network-lab
laboratorio de redes linux

