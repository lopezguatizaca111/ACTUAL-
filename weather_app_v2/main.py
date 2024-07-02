from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/segura")
def segura():
    if session:
      return render_template("segura.html")
    else:
        return redirect(url_for("login"))
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       return redirect(url_for("segura"))
    return render_template("login.html")

@app.route("/error")
def error():
    return render_template("error.html")



if __name__ =="__main__":
    app.run(debug=True)
