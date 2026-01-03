
import subprocess
import socket
import paramiko
import sys

print("########################################")
print("####### Realization ping and SSH ########")
print("########################################\n")

# 1. Pedir IP
host = input("Please introduce IP to connect: ")

# 2. Ping
print("\nDoing ping...\n")
ping = subprocess.run(
    ["ping", "-c", "3", host],
    capture_output=True,
    text=True
)

print(ping.stdout)

if ping.returncode != 0:
    print("Ping failed. Host unreachable.")
    sys.exit()

print("Ping successful!\n")

# 3. Verificar puerto
port = 22

while True:
    print(f"Trying port {port}...\n")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((host, port))
    sock.close()

    if result == 0:
        print(f"Port {port} is OPEN\n")
        break
    else:
        print(f"Port {port} is CLOSED")
        answer = input("Do you want try another port? (y/n): ")

        if answer.lower() == "y":
            port = int(input("Enter new port: "))
        else:
            print("Exiting program.")
            sys.exit()

# 4. Conexión SSH
print("\nTrying SSH connection...\n")

username = input("SSH username: ")
password = input("SSH password: ")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)

    print("SSH connection successful!\n")

    stdin, stdout, stderr = ssh.exec_command("uname -a")
    print(stdout.read().decode())

    ssh.close()

except Exception as e:
    print("SSH connection failed:")
    print(e)

