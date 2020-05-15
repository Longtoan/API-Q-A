from flask import current_app as app

# routes

@app.route("/")
def home():
    return "welcome Home"
