from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route("/")
# decorator - turns from normal
#python to function responding to
#local host
#def say_hello():
#  return "Hello world!"

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)
# automatically refreshs the page
# saves from killing and restarting
# app.run(debug=True)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)

@app.route("/newpage", methods=["POST"])
def new_page():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("newpage.html", form_data=data)


app.run(debug=True)
