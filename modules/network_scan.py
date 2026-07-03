import subprocess

def run_scan(target):
    """
    Runs an Nmap service detection scan on the target IP.
    Returns the scan results as text.
    """

    command = ["nmap", "-sV", target]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    with open("logs/nmap_scan.txt", "w") as file:
        file.write(result.stdout)

    return result.stdout