# 🛡️ CyberSOC Monitoring Platform

A Flask-based Cyber Security Monitoring Platform developed to simulate the basic functionalities of a Security Operations Center (SOC). The platform integrates multiple cybersecurity modules such as network scanning, traffic monitoring, phishing detection, firewall log analysis, SIEM dashboard, alert management, and PDF report generation into a single web application.

---

## 📖 Project Overview

CyberSOC Monitoring Platform is designed to demonstrate how different cybersecurity tools work together in a centralized monitoring system.

The application provides an interactive web interface where users can:

- Perform network scanning
- Monitor live network traffic
- Detect phishing emails and malicious URLs
- Analyze firewall logs
- View security alerts
- Generate security reports

---

## ✨ Features

- 🔍 Network Port Scanner (Nmap)
- 🌐 Live Traffic Monitoring (Scapy)
- 📧 Phishing Detection
- 🔥 Firewall Log Analysis
- 🚨 Security Alerts
- 📊 SIEM Dashboard
- 📈 CyberSOC Dashboard
- 📄 PDF Report Generation
- 📝 Log File Management

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Bootstrap 5
- Nmap
- Scapy
- ReportLab
- Git
- GitHub
- Kali Linux (VirtualBox)
- Visual Studio Code

---

## 📂 Project Structure

```text
CyberSOC-Monitoring-Platform
│
├── app.py
├── modules/
├── templates/
├── static/
├── logs/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Modules

### 🏠 Dashboard
Displays:
- System Status
- Quick Actions
- Module Status
- Recent Activity

### 🔍 Network Scanner
- Scans target hosts using Nmap
- Detects open ports
- Stores scan logs

### 🌐 Traffic Monitor
- Captures network packets using Scapy
- Displays Source IP, Destination IP and Protocol
- Saves captured traffic into logs

### 🔥 Firewall Log Analysis
- Reads firewall log files
- Displays firewall events

### 📧 Phishing Detection
Checks emails and URLs for:
- Suspicious keywords
- HTTP links
- IP addresses
- Long URLs
- Multiple hyphens

Returns:
- LOW Risk
- MEDIUM Risk
- HIGH Risk

### 🚨 Alerts
Generates security alerts from collected data.

### 📊 SIEM Dashboard
Shows:
- Total Hosts
- Open Ports
- Alerts
- Firewall Events
- Recent Security Events

### 📄 Reports
Generates a PDF security report summarizing the collected information.

---

# 📸 Screenshots

# 📸 Screenshots

## Dashboard

### Main Dashboard
![Dashboard](screenshots/dashboard.png)

### Dashboard - Module Status & Recent Activity
![Dashboard Bottom](screenshots/dashboard(bottom).png)

---

## Network Scanner

![Network Scanner](screenshots/network_scan.png)

---

## Traffic Monitor

![Traffic Monitor](screenshots/traffic.png)

---

## Firewall Log Analysis

![Firewall Logs](screenshots/firewall.png)

---

## Phishing Detection

### Phishing Detection - Input
![Phishing Input](screenshots/phishing(up).png)

### Phishing Detection - Result
![Phishing Result](screenshots/phishing(bottom).png)

---

## Alerts

![Alerts](screenshots/alerts.png)

---

## SIEM Dashboard

![SIEM Dashboard](screenshots/siem.png)

---

## Reports

![Reports](screenshots/reports.png)

---

## Generated PDF Report

### PDF Report - Page 1
![PDF Top](screenshots/pdf(up).png)

### PDF Report - Page 2
![PDF Bottom](screenshots/pdf(bottom).png)

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/NidhiyaS25/CyberSOC-Monitoring-Platform.git
```

Move into the project

```bash
cd CyberSOC-Monitoring-Platform
```

Create virtual environment

```bash
python3 -m venv venv
```

Activate virtual environment

Linux:

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 💡 Future Enhancements

- User Authentication
- Database Integration
- Real-time Dashboard
- Email Notifications
- Interactive Graphs
- Threat Intelligence APIs
- Machine Learning-based Threat Detection

---

## 👩‍💻 Author

**Nidhiya Naseer**

B.Tech Computer Science Student

Cybersecurity Enthusiast

GitHub:
https://github.com/NidhiyaS25

---

## 📌 Note

This project was developed as part of my cybersecurity learning journey to gain practical experience with Python, Flask, networking, and security monitoring concepts.