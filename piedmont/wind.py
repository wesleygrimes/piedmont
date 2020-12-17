from piedmont import services
from flask import Blueprint
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from werkzeug.exceptions import abort

bp = Blueprint("wind", __name__)


@bp.route("/")
def index():
    """Fetch wind plots"""
    plots = {"grandfather_wind_barb": services.get_grandfather_wind_barb()}

    return render_template("wind/index.html", plots=plots)
