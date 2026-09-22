from flask import Flask,render_template

app = Flask(__name__)



@app.route("/")
def hi_template_render():
    return render_template("hb.html")

@app.route("/profile")
def profile():
    hobbies=["영화 감상","여행 가기","음악 감상"]
    return render_template("profile.html",hobbies=hobbies)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)