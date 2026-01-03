# DNS Configuration

## Overview

In this lab, the goal was to configure a **local DNS server** using `bind9` to allow name resolution between the server and client VM in an isolated network. The DNS configuration included both **forward (domain to IP) and reverse (IP to domain) zones**, enabling proper translation of hostnames and IP addresses within the lab.  

Since the client has no internet access, this DNS server functions solely for internal name resolution between the server and client. No conflicts with DHCP or firewall occurred, except that **port 53** needed to be allowed in the firewall for DNS communication.

---

## Configuration

- **DNS Server:** `bind9` on the server VM (IP 192.168.100.2)  
- **Forward Zone:** Resolves `server.lab.local` → `192.168.100.2`  
- **Reverse Zone:** Resolves `192.168.100.2` → `server.lab.local`  
- **Firewall:** Port 53 enabled for both TCP and UDP  

**Example commands to verify DNS resolution:**

```bash
# Reverse lookup: IP → hostname
dig @127.0.0.1 -x 192.168.100.2

# Forward lookup: hostname → IP
dig @127.0.0.1 server.lab.local

#Sample Output:
lautaro@debian:~$ dig @127.0.0.1 -x 192.168.100.2
...
;; ANSWER SECTION:
2.100.168.192.in-addr.arpa. 604800 IN PTR server.lab.local.

lautaro@debian:~$ dig @127.0.0.1 server.lab.local
...
;; ANSWER SECTION:
server.lab.local. 604800 IN A 192.168.100.2

#Verification

Confirmed that forward and reverse DNS queries return correct results.

Ensured the DNS server resolves names only for the internal network (lab-local).

Verified that enabling port 53 in the firewall allows communication without interfering with DHCP or other services.

