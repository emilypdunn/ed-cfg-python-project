from flask import Flask, render_template, request
import os

app = Flask(__name__)

# app = Flask(static_folder='static')

#@app.route("/")
# decorator - turns from normal
#python to function responding to
#local host
#def say_hello():
#  return "Hello world!"

@app.route("/")
def iniial_page():
  return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)

@app.route("/female.html")
def female():
  return render_template("female.html")

@app.route("/aboutUs.html")
def about_us():
  return render_template("aboutUs.html")

@app.route("/newpage", methods=["POST"])
def new_page():
  data = request.values
  return render_template("newpage.html", form_data=data)


if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)