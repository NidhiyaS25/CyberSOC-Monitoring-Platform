import os

def read_firewall_logs():

    if not os.path.exists("logs/firewall.log"):
        return ["No firewall log available."]

    with open("logs/firewall.log", "r") as file:
        logs = file.readlines()

    return logs