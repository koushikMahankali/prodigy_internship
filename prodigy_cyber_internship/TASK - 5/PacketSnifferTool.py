#PacketSniffingTool Using Scapy Module In Python
#To Run In This Tool In Windows Use Ncap Application For Sniffing 
from scapy.layers.inet import *
from scapy.all import *
from colorama import Fore, Back

# Packet callback function
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        log_data = Back.BLACK + Fore.RED + f"Source IP: {src_ip} --> Destination IP: {dst_ip} | Protocol: {proto}\n"
        if TCP in packet:
            payload = packet[TCP].payload
            log_data += Fore.GREEN + f"TCP Payload: {payload}\n"
        elif UDP in packet:
            payload = packet[UDP].payload
            log_data += Fore.YELLOW + f"UDP Payload: {payload}\n"
        elif ICMP in packet:
            payload = packet[ICMP].payload
            log_data += Fore.CYAN + f"ICMP Payload: {payload}\n"

        print(log_data)  # Print to console
        with open("packet_log.txt", "a") as log_file:
            log_file.write(log_data)
        print("Packet logged.")

try:
    print("Starting packet sniffing...")
    print(Back.WHITE + "Press Ctrl+C to stop.")
    sniff(prn=packet_callback, filter="ip")
except KeyboardInterrupt:
    print("Packet sniffing interrupted by user. Exiting.")