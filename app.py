
from flask import Flask, render_template, request
from modules.network_scan import run_scan
from modules.traffic_monitor import capture_packets
from modules.firewall_logs import read_firewall_logs
from modules.siem_dashboard import get_siem_data
from modules.phishing_detector import detect_phishing
from modules.alerts import generate_alerts
from modules.report_generator import generate_report
from modules.pdf_generator import create_pdf
from flask import send_file
from modules.dashboard import get_dashboard_data
app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
def dashboard():

    modules, activity = get_dashboard_data()

    return render_template(
        "dashboard.html",
        modules=modules,
        activity=activity
    )


@app.route("/network_scan", methods=["GET", "POST"])
def network_scan():

    result = ""
    target = ""

    if request.method == "POST":

        target = request.form["target"]

        result = run_scan(target)

    return render_template(
        "network_scan.html",
        result=result,
        target=target
    )


@app.route("/traffic", methods=["GET", "POST"])
def traffic():

    result = ""

    if request.method == "POST":
        result = capture_packets()

    return render_template(
        "traffic.html",
        result=result
    )


@app.route("/firewall", methods=["GET", "POST"])
def firewall():

    logs = ""

    if request.method == "POST":
        logs = read_firewall_logs()

    return render_template(
        "firewall.html",
        logs=logs
    )


@app.route("/siem")
def siem():

    data = get_siem_data()
    alerts = generate_alerts()

    return render_template(
        "siem.html",
        data=data,
        alerts=alerts
    )

@app.route("/phishing", methods=["GET", "POST"])
def phishing():

    risk = ""
    email_keywords = []
    url_findings = []
    error = ""

    if request.method == "POST":

        email_text = request.form.get("email", "").strip()
        url = request.form.get("url", "").strip()

        if not email_text and not url:
            error = "Please enter an email, a URL, or both."

        else:
            risk, email_keywords, url_findings = detect_phishing(
                email_text,
                url
            )

    return render_template(
        "phishing.html",
        risk=risk,
        email_keywords=email_keywords,
        url_findings=url_findings,
        error=error
    )


@app.route("/alerts")
def alerts():

    alerts = generate_alerts()

    return render_template(
        "alerts.html",
        alerts=alerts
    )


@app.route("/reports", methods=["GET", "POST"])
def reports():

    report = ""

    if request.method == "POST":

        action = request.form.get("action")

        report = generate_report()

        if action == "download":

            filename = create_pdf()

            return send_file(
                filename,
                as_attachment=True
            )

    return render_template(
        "reports.html",
        report=report
    )

if __name__ == "__main__":
    app.run(debug=True)