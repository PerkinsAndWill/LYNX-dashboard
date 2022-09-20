from flask import Flask, redirect, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

tabs = {
    "otp": {
        "name": "otp",
        "url": "./otp",
        "descriptive_name": "On Time Performance",
        "image_name": "lynx-otp-icon.png",
        "tableau_name": "/LynxOTP/SystemOTP",
    },
    "runtime_time": {
        "name": "runtime_time",
        "url": "./runtime_time",
        "descriptive_name": "Run Time - By Period",
        "image_name": "lynx-runtime-time-icon.png",
        "tableau_name": "/LynxRunningTime/LynxRunningTime",
    },
    "runtime_trip": {
        "name": "runtime_trip",
        "url": "./runtime_trip",
        "descriptive_name": "Run Time - By Trip",
        "image_name": "lynx-runtime-trip-icon.png",
        "tableau_name": "/LynxRunningTimebyTrip/LynxRunningTime",
    },
}


@app.route("/")
def home():
    return render_template(
        "main.html", length=len(tabs), tabs=list(tabs.values()), page="main"
    )


@app.route("/<template_name>")
def index(template_name):
    if template_name not in tabs:
        return redirect("./", code=302)
    return render_template(
        "tableau.html",
        length=len(tabs),
        tabs=list(tabs.values()),
        tableau_name=tabs[template_name]["tableau_name"],
        page=template_name,
    )
