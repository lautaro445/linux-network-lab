version en español
# Linux Network Lab

Laboratorio práctico de redes y administración de sistemas Linux realizado sobre máquinas virtuales Debian minimal utilizando KVM.

## Objetivo
Construir un entorno cliente-servidor funcional para el estudio práctico de:
- Redes
- Servicios esenciales
- Seguridad
- Automatización básica

## Tecnologías
- Debian GNU/Linux (VMs)
- KVM / libvirt
- SSH
- DHCP
- DNS (BIND9)
- iptables
- Python

## Topología
- Host: Xubuntu
- VM Server: Debian minimal
- VM Client: Debian minimal
- Red aislada: lab-local

## Servicios implementados
- IP estática
- SSH con autenticación por clave
- DHCP server
- DNS directo e inverso
- Firewall básico
- Script de automatización en Python

## Estado actual
- Resolución DNS interna funcional
- Sin salida a Internet desde cliente (pendiente de corrección)

## Próximas mejoras
- Corrección de forwarding/NAT para salida a Internet
- Automatización avanzada
- Nuevos clientes
- Integración con bases de datos
