from flask import Flask, render_template, request

app = Flask(__name__)
contact_info = {
    "email": "youremail@example.com",
    "phone": "123-456-7890",
    "github": "github.com/yourusername"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_cps", methods=["POST"])
def check_cps():
    start_time = request.form["start_time"]
    end_time = request.form["end_time"]
    clicks = request.form["clicks"]

    try:
        cps = int(clicks) / (int(end_time) - int(start_time))
    except ValueError:
        cps = 0

    return render_template("result.html", cps=cps)

@app.route("/")
def index():
    return render_template("indexx.html", contact_info=contact_info)

if __name__ == "__main__":
    app.run(debug=True)