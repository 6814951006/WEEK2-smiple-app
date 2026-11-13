from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
LOG_FILE = Path(__file__).with_name("log.txt")


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    error = None

    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if not message:
            error = "กรุณากรอกข้อความก่อนส่ง"
            return render_template("index.html", error=error), 400

        with LOG_FILE.open("a", encoding="utf-8") as log_file:
            log_file.write(f"{message}\n")

    return render_template("index.html", message=message, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
