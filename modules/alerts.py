def generate_alerts():

    alerts = []

    # Network Scan Alerts
    try:
        with open("logs/nmap_scan.txt", "r") as file:

            content = file.read()

            open_ports = content.count(" open ")

            if open_ports >= 5:
                alerts.append({
                    "severity": "HIGH",
                    "module": "Network Scan",
                    "message": f"{open_ports} open ports detected."
                })

            elif open_ports >= 1:
                alerts.append({
                    "severity": "LOW",
                    "module": "Network Scan",
                    "message": f"{open_ports} open port(s) detected."
                })

    except FileNotFoundError:
        pass

    # Firewall Alerts
    try:
        with open("logs/firewall.log", "r") as file:

            firewall_events = len(file.readlines())

            if firewall_events > 0:
                alerts.append({
                    "severity": "LOW",
                    "module": "Firewall",
                    "message": f"{firewall_events} firewall log entries found."
                })

    except FileNotFoundError:
        pass

    return alerts