import flask
import os

# Create the web server
app = flask.Flask(__name__)

# Create a route handler
@app.route("/")
def hello():
    return flask.render_template("index.html")

@app.route("/amaydle")
def hi():
    return "<h1> Hello I'm Amaydle </h1>"

@app.route("/open/spotify")
def open_spotify():
    os.system("open /Applications/spotify.app")
    return ""

@app.route("/close/spotify")
def close_spotify():
    os.system("killall Spotify")
    return ""
# Run the server
app.run(debug=True)