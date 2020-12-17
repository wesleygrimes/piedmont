from piedmont import services
from flask import Blueprint
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from werkzeug.exceptions import abort

bp = Blueprint("temperature", __name__)


@bp.route("/")
def index():
    """Fetch temperature plots"""
    plots = {"nc_mountain_temperature_plot": services.get_nc_mountain_temperature_plot(),
             "nc_piedmont_temperature_plot": services.get_nc_mountain_temperature_plot(),
             "va_piedmont_temperature_plot": services.get_nc_mountain_temperature_plot()
             }

    return render_template("temperature/index.html", plots=plots)
