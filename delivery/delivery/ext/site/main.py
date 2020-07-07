from flask import request, render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

# Geraldo Luiz - testando git


@bp.route("/")
def index():
    name = "Geraldo"
    # return render_template("index.html", name=request.args["name"])
    return render_template("index.html", name=name)
