# vim: set fileencoding=utf-8

from flask import Flask, render_template, session, redirect, request
import furoshiki

app = Flask(__name__)
app.config["SECRET_KEY"] = furoshiki.CONFIG.SECRET_KEY

def get_config():
    config = furoshiki.CONFIG
    config.IS_LOGIN = is_login()
    config.TEMPLATE = dict()
    config.TEMPLATE["header_nav_account_is_active"] = request.path == "/account"
    return config

def is_login():
    return "email" in session


def get_templatedata():
    return {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/account")
def account():
    return render_template("account.html", config=get_config())

@app.route("/admin")
def admin():
    return render_template("admin.html", config=get_config())


@app.before_request
def login_check():
    if request.path.startswith("/static"):
        return
    if request.endpoint in ("account", "admin"):
        return
    if not is_login():
        return redirect("/account")


if __name__ == "__main__":
    app.debug = True
    app.run()
