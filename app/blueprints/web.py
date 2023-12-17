from flask import Blueprint, request

bp = Blueprint("web",__name__)

@bp.route("/")
def index():
    return "<p>Hello, World!</p>"

