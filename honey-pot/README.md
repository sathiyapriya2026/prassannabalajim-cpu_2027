# 🍯 Python Honeypot

A lightweight, multi-service honeypot written in Python that simulates SSH, FTP, HTTP, and Telnet services to detect and log unauthorized access attempts. Designed for educational purposes and defensive security research.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Security](https://img.shields.io/badge/Purpose-Defensive%20Security-red)

---

## 📸 Preview

```
==================================================
       Simple Python Honeypot v2.0
==================================================
[+] Decoy file created: honeypot_data/passwords.txt
[+] Decoy file created: honeypot_data/config.json
[+] Decoy file created: honeypot_data/id_rsa

[*] Listening on port 2222 (SSH)
[*] Listening on port 2121 (FTP)
[*] Listening on port 8080 (HTTP)
[*] Listening on port 2323 (Telnet)

[*] Honeypot active. Press Ctrl+C to stop.
```

---

## 🚀 Features

- **Multi-Service Simulation** — Mimics SSH, FTP, HTTP, and Telnet services
- **Fake Decoy Files** — Auto-generates realistic lure files (passwords, SSH keys, configs, etc.)
- **Real-Time Logging** — Captures attacker IP, port, timestamp, and all data sent
- **Fake Banners** — Sends convincing service banners to attract attackers
- **Multi-threaded** — Handles multiple simultaneous connections
- **Multi-stage Auth Capture** — Captures both username AND password for FTP/Telnet
- **Zero Dependencies** — Uses only Python standard library

---

## 📁 Project Structure

```
python-honeypot/
├── honeypot.py            ← Main honeypot script
├── requirements.txt       ← Python dependencies (standard lib only)
├── README.md              ← Project documentation
├── .gitignore             ← Files to exclude from Git
├── LICENSE                ← MIT License
└── honeypot_data/         ← Auto-generated decoy files (on run)
    ├── passwords.txt
    ├── users.txt
    ├── config.json
    ├── id_rsa
    └── credit_cards.csv
```

---

## ⚙️ Requirements

- Python 3.6+
- Kali Linux / Ubuntu / any Linux distro
- No third-party packages required

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/python-honeypot.git
cd python-honeypot
```

### 2. (Optional) Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Honeypot
```bash
python3 honeypot.py
```

### 5. Run with Root (for real service ports 22, 21, 80, 23)
```bash
sudo python3 honeypot.py
```

---

## 🧪 Testing the Honeypot

Open a second terminal and simulate attacker connections:

```bash
# Test SSH
nc localhost 2222

# Test FTP
nc localhost 2121

# Test HTTP
curl http://localhost:8080

# Test Telnet
nc localhost 2323
```

---

## 📊 Monitoring Logs

```bash
# Watch logs in real time
tail -f honeypot.log

# View all logs
cat honeypot.log
```

### Sample Log Output
```
2024-01-15 14:32:01 - ==================================================
2024-01-15 14:32:01 - [+] NEW CONNECTION
2024-01-15 14:32:01 -     Time     : 2024-01-15 14:32:01
2024-01-15 14:32:01 -     Source IP: 192.168.1.100:54321
2024-01-15 14:32:01 -     Port Hit : 2222 (SSH)
2024-01-15 14:32:01 - [!!!] DATA RECEIVED from 192.168.1.100:54321
2024-01-15 14:32:01 -       Decoded: root
```

---

## 🔧 Configuration

Edit the `PORTS` list in `honeypot.py` to change which ports are monitored:

```python
# Default (no root needed)
PORTS = [2222, 2121, 8080, 2323]

# Real service ports (requires root/sudo)
PORTS = [22, 21, 80, 23]
```

---

## 🖥️ Running in Background (Kali Linux)

```bash
# Using nohup
nohup python3 honeypot.py &

# Using screen
screen -S honeypot
python3 honeypot.py
# Detach: Ctrl+A then D
# Reattach: screen -r honeypot
```

---

## 🔥 Firewall Setup (Optional)

```bash
sudo ufw allow 2222
sudo ufw allow 2121
sudo ufw allow 8080
sudo ufw allow 2323
sudo ufw enable
sudo ufw status
```

---

## ⚠️ Legal Disclaimer

> This tool is intended for **educational purposes and defensive security research only**.
> Only deploy this honeypot on systems and networks **you own or have explicit written permission** to monitor.
> Unauthorized use against systems you do not own is **illegal** and may result in criminal prosecution.
> The author takes **no responsibility** for misuse of this tool.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

Made with ❤️ for the cybersecurity community.
