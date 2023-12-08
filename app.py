from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("home.html")

@app.route('/projects')
def projects_page():
  return render_template("projects.html")

@app.route('/contact')
def contact_page():
  return render_template("contact.html")

app.run(host='0.0.0.0', port=81, debug=True)
