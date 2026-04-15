# Network Intrusion Detection System (NIDS)

This is a simple project I built to understand how network security
works in real time.

The idea is to monitor network traffic, detect suspicious activity like
port scanning, and take action against it.

## What this project does

-   Captures live network traffic using Scapy\
-   Tracks how many ports an IP is trying to access\
-   If an IP tries too many ports, it is treated as a port scan\
-   Logs the alert in a file\
-   Blocks the IP using iptables (Linux)

## Why I built this

I wanted to learn how intrusion detection systems actually work instead
of just reading theory.\
So I tried building a small version of it using Python.

## Tech used

-   Python\
-   Scapy\
-   Linux (iptables)

## How to run

sudo python3 main.py

Root access is required for packet sniffing and blocking IPs.

## Sample output

\[ALERT\] Port Scan Detected from 192.168.1.5

## Future improvements

-   Add more attack detection\
-   Better logging system\
-   Maybe a simple dashboard

## Author

Aman Parashar
