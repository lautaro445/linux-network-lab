# VM Setup and SSH Configuration

## Overview

In this phase, two KVM virtual machines (VMs) were created on the Xubuntu host. The main goal was to establish basic network connectivity and remote management using SSH.

## Steps Performed

### 1. VM Creation

- Two VMs were created using KVM.
- Basic Linux commands were tested:
  - `ip a` to check network interfaces
  - `ip route` to view routing tables
  - `ping` to test connectivity

### 2. IP Configuration

- Initial pings between VMs and the host failed.
- Fixed IP addresses were assigned manually to ensure connectivity:
  - Host ↔ VM1 ↔ VM2
- After assigning static IPs, ping tests were successful.

### 3. SSH Setup

- SSH was used for remote access and easier configuration management.
- Steps:
  1. Installed `openssh-server` if not already present.
  2. Connected via SSH from host to VMs:  
     ```bash
     ssh user@vm_ip
     ```
  3. Used `scp` to transfer files between host and VMs:
     ```bash
     scp localfile user@vm_ip:/remote/path
     ```
  4. For practice, the SSH port on the client VM was changed from default `22` to `2222`:
     ```bash
     sudo nano /etc/ssh/sshd_config
     # Change Port 22 to Port 2222
     sudo systemctl restart ssh
     ```

### Notes / Lessons Learned

- Manually assigning IPs is crucial when initial network configuration fails.
- SSH is essential for managing multiple VMs efficiently.
- Changing the SSH port is a good practice for learning security basics.

---
#######################################################################################################
##############################################################################################################################################
##########################################################################

# Configuración de VMs y SSH (Español)

## Resumen

En esta fase se crearon dos máquinas virtuales (VMs) en KVM sobre un host Xubuntu. El objetivo principal fue establecer conectividad básica y administración remota mediante SSH.

## Pasos Realizados

### 1. Creación de VMs

- Se crearon dos VMs usando KVM.
- Se probaron comandos básicos de Linux:
  - `ip a` para ver interfaces de red
  - `ip route` para ver rutas de red
  - `ping` para probar conectividad

### 2. Configuración de IP

- Inicialmente los pings entre host y VMs fallaban.
- Se asignaron direcciones IP fijas manualmente:
  - Host ↔ VM1 ↔ VM2
- Tras asignar IPs estáticas, los pings fueron exitosos.

### 3. Configuración de SSH

- Se utilizó SSH para acceder remotamente y facilitar la gestión de archivos.
- Pasos:
  1. Instalar `openssh-server` si no estaba presente.
  2. Conexión SSH desde host a VMs:
     ```bash
     ssh usuario@ip_vm
     ```
  3. Uso de `scp` para transferir archivos:
     ```bash
     scp archivo_local usuario@ip_vm:/ruta/remota
     ```
  4. Para practicar, se cambió el puerto SSH del cliente de `22` a `2222`:
     ```bash
     sudo nano /etc/ssh/sshd_config
     # Cambiar Port 22 a Port 2222
     sudo systemctl restart ssh
     ```
