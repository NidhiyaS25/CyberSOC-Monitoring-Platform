from modules.alerts import generate_alerts
def get_siem_data():

    hosts = 0
    ports = 0

    try:
        with open("logs/nmap_scan.txt", "r") as file:

            content = file.readlines()

            for line in content:

                if "Nmap scan report for" in line:
                    hosts += 1

                if "/tcp" in line and "open" in line:
                    ports += 1

    except FileNotFoundError:
        pass

    try:
        with open("logs/firewall.log", "r") as file:
            firewall = len(file.readlines())
    except FileNotFoundError:
        firewall = 0

    alerts = generate_alerts()

    data = {
        "hosts": hosts,
        "ports": ports,
        "alerts": len(alerts),
        "firewall": firewall
    }

    return data