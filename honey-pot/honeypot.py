import socket
import threading
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="honeypot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(msg):
    print(msg)
    logging.info(msg)

def handle_client(conn, addr, port):
    ip, client_port = addr
    log(f"[+] Connection from {ip}:{client_port} on port {port}")

    try:
        # Send a fake SSH/service banner
        if port == 22:
            conn.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n")
        elif port == 21:
            conn.send(b"220 FTP Server Ready\r\n")
        elif port == 80:
            conn.send(b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.41\r\n\r\n<html>Welcome</html>")
        elif port == 23:
            conn.send(b"Welcome to Telnet Service\r\nlogin: ")

        # Try to receive data (credentials or commands)
        data = conn.recv(1024)
        if data:
            log(f"[DATA] From {ip}:{client_port} on port {port} => {data!r}")
    except Exception as e:
        log(f"[ERROR] {ip}:{client_port} - {e}")
    finally:
        conn.close()
        log(f"[-] Connection closed from {ip}:{client_port}")

def start_listener(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind(("0.0.0.0", port))
        server.listen(5)
        log(f"[*] Honeypot listening on port {port}")
        while True:
            conn, addr = server.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr, port))
            t.daemon = True
            t.start()
    except PermissionError:
        print(f"[!] Permission denied on port {port}. Run as root or use ports > 1024.")
    except OSError as e:
        print(f"[!] Port {port} error: {e}")

if __name__ == "__main__":
    # Ports to listen on (simulating common services)
    PORTS = [2222, 2121, 8080, 2323]  # High ports (no root needed)
    # For real ports (22, 21, 80, 23) you need root/admin

    print("=" * 40)
    print("  Simple Python Honeypot")
    print("=" * 40)

    threads = []
    for port in PORTS:
        t = threading.Thread(target=start_listener, args=(port,))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\n[!] Honeypot shutting down.")