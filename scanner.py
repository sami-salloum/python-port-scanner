import socket

IP = input("Enter target IP: ")

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((IP, port))
        print(f"[+] Port {port} is open")
    except:
        continue
    s.close()
