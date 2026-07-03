from datetime import datetime
from modules.siem_dashboard import get_siem_data
from modules.alerts import generate_alerts


def generate_report():

    data = get_siem_data()
    alerts = generate_alerts()

    report = ""

    report += "CyberSecurity Monitoring Report\n"
    report += "=" * 45 + "\n\n"

    report += f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"

    report += "NETWORK SUMMARY\n"
    report += "-" * 45 + "\n"
    report += f"Hosts Scanned : {data['hosts']}\n"
    report += f"Open Ports    : {data['ports']}\n"
    report += f"Firewall Logs : {data['firewall']}\n"
    report += f"Alerts        : {data['alerts']}\n\n"

    report += "SECURITY ALERTS\n"
    report += "-" * 45 + "\n"

    if alerts:
        for alert in alerts:
            report += f"[{alert['severity']}] {alert['module']} - {alert['message']}\n"
    else:
        report += "No alerts generated.\n"

    return report