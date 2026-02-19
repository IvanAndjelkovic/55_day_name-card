from flask import Flask, render_template

app = Flask(__name___)

@app.route("/"):
def starting_page():
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(debug=True)