from flask import flask,render_template

app=flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)