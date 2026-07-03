import subprocess
import shutil
import os

def run_scan(target):

    if shutil.which("nmap") is None:
        return "Nmap is not available on this server. This feature works only in the local Kali environment."

    try:
        result = subprocess.check_output(
            ["nmap", "-F", target],
            text=True
        )

        os.makedirs("logs", exist_ok=True)

        with open("logs/nmap_scan.txt", "w") as file:
            file.write(result)

        return result

    except Exception as e:
        return f"Error: {e}"