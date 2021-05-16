from flask import Blueprint, send_from_directory

client = Blueprint("client", __name__)


# Main web page
@client.route("/")
@client.errorhandler(404)
def base(*args):
    return send_from_directory("spa", "__app.html")


# Path for all the static files
@client.route("/<path:path>")
def home(path):
    return send_from_directory("spa", path)
