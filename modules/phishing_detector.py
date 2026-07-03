import re

def detect_phishing(email_text, url):

    email_keywords = [
        "urgent",
        "verify",
        "click here",
        "bank",
        "password",
        "account suspended",
        "login now"
    ]

    email_found = []

    for keyword in email_keywords:

        if keyword.lower() in email_text.lower():
            email_found.append(keyword)

    url_found = []

    # Uses HTTP instead of HTTPS
    if url.startswith("http://"):
        url_found.append("Uses HTTP")

    # Contains IP address
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        url_found.append("Uses IP Address")

    # Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "account"
    ]

    for word in suspicious_words:

        if word in url.lower():
            url_found.append(f'Contains "{word}"')

    # Too many hyphens
    if url.count("-") >= 2:
        url_found.append("Too many hyphens")

    # Long URL
    if len(url) > 60:
        url_found.append("Very long URL")

    score = len(email_found) + len(url_found)

    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # Save phishing scan log
    with open("logs/phishing_log.txt", "w") as file:

        file.write(f"Risk Level: {risk}\n\n")

        file.write("Email Findings:\n")
        for item in email_found:
            file.write(f"- {item}\n")

        file.write("\nURL Findings:\n")
        for item in url_found:
            file.write(f"- {item}\n")

    return risk, email_found, url_found