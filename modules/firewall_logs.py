def read_firewall_logs():

    logs = []

    with open("logs/firewall.log", "r") as file:

        for line in file:

            parts = line.strip().split()

            logs.append({
                "date": parts[0],
                "time": parts[1],
                "action": parts[2],
                "ip": parts[3]
            })

    return logs