import os
from modules.siem_dashboard import get_siem_data


def get_dashboard_data():

    data = get_siem_data()

    modules = [

        {
            "name": "Network Scan",
            "status": "Completed" if os.path.exists("logs/nmap_scan.txt") else "Not Run"
        },

        {
            "name": "Traffic Monitor",
            "status": "Completed" if os.path.exists("logs/traffic_log.txt") else "Not Started"
        },

        {
            "name": "Firewall Logs",
            "status": f"{data['firewall']} Log(s)" if data["firewall"] > 0 else "No Logs"
        },

        {
            "name": "Phishing Detection",
            "status": "Completed" if os.path.exists("logs/phishing_log.txt") else "Not Scanned"
        },

        {
            "name": "Alerts",
            "status": f"{data['alerts']} Alert(s)" if data["alerts"] > 0 else "No Alerts"
        },

        {
            "name": "Reports",
            "status": "Generated" if os.path.exists("CyberSecurity_Report.pdf") else "Not Generated"
        }

    ]

    activity = []

    if os.path.exists("logs/nmap_scan.txt"):
        activity.append("Network scan completed successfully.")

    if data["firewall"] > 0:
        activity.append(f"{data['firewall']} firewall log(s) loaded.")

    if data["alerts"] > 0:
        activity.append(f"{data['alerts']} security alert(s) generated.")

    if not activity:
        activity.append("System started successfully.")

    return modules, activity