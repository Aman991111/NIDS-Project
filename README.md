🔐 Real-Time Network Intrusion Detection & Prevention System (NIDS + IPS)

📌 Overview

This project is a real-time Network Intrusion Detection and Prevention System (NIDS + IPS) built using Python and Scapy. It monitors live network traffic, detects suspicious activities such as port scanning, and automatically blocks malicious IP addresses using iptables.

Features

- Real-time packet sniffing and analysis
- Detection of port scanning attacks
- Automated IP blocking using iptables
- Logging of suspicious activities
- Attack simulation using Nmap

 Technologies Used

- Python
- Scapy
- Nmap
- Linux (iptables)

How to Run

1. Clone the repository

git clone https://github.com/Aman991111/NIDS-Project
cd NIDS-Project

2. Install dependencies

pip install scapy

3. Run the project

sudo python3 main.py

Example Output

[ALERT] Port Scan Detected from IP: 192.168.1.5
[ACTION] Blocking IP using iptables...
[LOG] Entry saved for security auditing

Project Structure

NIDS-Project/
│── main.py
│── logger.py
│── README.md

Skills Demonstrated

- Network Traffic Analysis
- Intrusion Detection Systems (NIDS)
- Intrusion Prevention Systems (IPS)
- Cybersecurity Monitoring
- Linux Firewall (iptables)

Author

Aman Parashar
