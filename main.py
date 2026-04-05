import os
from scapy.all import sniff, IP, TCP
from collections import defaultdict
from logger import log_alert

ip_ports = defaultdict(set)
alerted = set()

def block_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")

def detect(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src = packet[IP].src
        port = packet[TCP].dport

        ip_ports[src].add(port)

        if len(ip_ports[src]) > 10 and src not in alerted:
           msg = f"[ALERT] Port Scan Detacted from {src}"
           print(msg)
           log_alert(msg)

           block_ip(src)
           alerted.add(src)

sniff(prn=detect)
