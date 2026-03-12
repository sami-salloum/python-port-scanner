# 🔍 Python Port Scanner

A lightweight, fast TCP port scanner built from scratch in Python — no external libraries required.

Built to understand how network reconnaissance tools like Nmap work under the hood.

---

## 📌 Features

- Scans any target IP address for open TCP ports
- Covers ports 1–1024 by default
- Fast socket-based scanning with configurable timeout
- Clean output — only displays open ports
- Zero external dependencies (uses Python's built-in `socket` module)

---

## 🚀 Usage

```bash
python scanner.py
```

You will be prompted to enter a target IP:

```
Enter target IP: 192.168.1.1

[+] Port 22 is open
[+] Port 80 is open
[+] Port 443 is open

Scan complete.
```

---

## 🛠️ How It Works

The scanner creates a TCP socket and attempts to connect to each port on the target machine.

- If the connection **succeeds** → port is open
- If the connection **fails** (refused/timeout) → port is closed and skipped

This mirrors the core logic behind a TCP Connect Scan (`nmap -sT`).

```python
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
```

---

## 📚 What I Learned

- How TCP connections work at the socket level (SYN → SYN-ACK → RST)
- How port scanning tools like Nmap work under the hood
- Python socket programming and exception handling
- The importance of timeouts in network programming

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.  
Only scan systems you own or have explicit permission to test.  
Unauthorized port scanning may be illegal in your jurisdiction.

---

## 👤 Author

**Sami Salloum**  
CS Student | Ethical Hacking & Penetration Testing Enthusiast  
🔗 [LinkedIn](https://linkedin.com/in/) • 🐙 [GitHub](https://github.com/)

---

## 📄 License

MIT License — free to use and modify with attribution.
