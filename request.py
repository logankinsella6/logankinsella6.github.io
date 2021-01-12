from flask import Flask, redirect, url_for

app = Flask(__name__)
name =


@app.route("/")
def home():
	return render_template("index.html", content=No)

if __name__ == "__main__":
	app.run()
