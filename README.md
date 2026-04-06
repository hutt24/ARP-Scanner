# ARP Scanner

A simple ARP scanner written in Python using Scapy.  
Scans a local subnet and lists the IP and MAC addresses of active devices.

## How it works
- Sends ARP broadcast requests to all IPs in the subnet
- Any online device will reply with its MAC address
- Uses Scapy to craft and receive Ethernet frames

## Example output

172.20.10.1 b6:ae:c1:39:bc:64
172.20.10.2 a8:3b:76:d7:01:c9


## Requirements
- Python 3.x
- Scapy (`pip install scapy`)
- Npcap (Windows) or libpcap (Linux/Mac)

## Usage
Run as administrator/root:

python arp_scanner.py
