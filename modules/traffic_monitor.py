from scapy.all import sniff
from datetime import datetime

def capture_packets():

    packets = sniff(count=7)

    output = ""

    for packet in packets:

        if packet.haslayer("IP"):

            time = datetime.now().strftime("%H:%M:%S")

            src = packet["IP"].src
            dst = packet["IP"].dst

            if packet.haslayer("TCP"):
                protocol = "TCP"
            elif packet.haslayer("UDP"):
                protocol = "UDP"
            elif packet.haslayer("ICMP"):
                protocol = "ICMP"
            else:
                protocol = "IP"

            output += f"{time:<10} {src:<18} {dst:<18} {protocol}\n"

    with open("logs/traffic_log.txt", "w") as file:
        file.write(output)

    return output