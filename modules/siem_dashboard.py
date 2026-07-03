import os

def get_siem_data():

    firewall = 0
    alerts = 0

    if os.path.exists("logs/firewall.log"):
        with open("logs/firewall.log", "r") as file:
            firewall = len(file.readlines())

    if os.path.exists("logs/alerts.txt"):
        with open("logs/alerts.txt", "r") as file:
            alerts = len(file.readlines())

    return {
        "firewall": firewall,
        "alerts": alerts
    }