from flask import request, render_template
from flask import Blueprint

from flask import current_app   # para debug (log)

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    current_app.logger.info("entrei na função index")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")
