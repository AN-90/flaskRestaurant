from flask import flask,render_template

app=flask(__name__)

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/")
def Menu():
    return render_template("Menu.html")

@app.route("/")
def Contact():
    return render_template("Contact.html")

if __name__=="__main__":
    app.run(debug=True)
