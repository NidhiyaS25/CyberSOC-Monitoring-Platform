import os

def generate_report():

    report = ""

    files = [
        "logs/nmap_scan.txt",
        "logs/traffic_log.txt",
        "logs/firewall.log",
        "logs/phishing_log.txt"
    ]

    for filename in files:

        report += "=" * 60 + "\n"
        report += filename + "\n"
        report += "=" * 60 + "\n"

        if os.path.exists(filename):

            with open(filename, "r") as file:
                report += file.read()

        else:
            report += "File not available.\n"

        report += "\n\n"

    return report