from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    url_for('static', filename='home-page.css')
    return render_template("index.html")


@app.route("/mission")
def mission():
    url_for('static', filename='mission.css')
    return render_template("missionStatement.html")


@app.route("/contact")
def contact():
    url_for('static', filename='contactUs.css')
    return render_template("contactUs.html")


@app.route("/prayer")
def prayer():
    url_for('static', filename='prayer.css')
    return render_template("prayerRequests.html")


@app.route("/donations")
def donations():
    url_for('static', filename='donations.css')
    return render_template("donations.html")


@app.route("/photo-gallery")
def gallery():
    url_for('static', filename='photo-gallery.css')
    return render_template("photo-gallery.html")


@app.route("/announcements")
def announcements():
    url_for('static', filename='announcements.css')
    return render_template("announcements.html")


if __name__ == "__main__":
    app.run(debug=True)
