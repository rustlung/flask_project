from flask import Blueprint, render_template

from app.models.experience import Experience
from app.models.timeline import Timeline

page_bp = Blueprint("page", __name__)


@page_bp.route("/", methods=["GET"])
def showcase():
    experiences = (
        Experience.query.filter_by(public=True)
        .order_by(Experience.start_date.desc())
        .all()
    )
    timeline_events = (
        Timeline.query.order_by(Timeline.order.desc().nullslast(), Timeline.date.desc()).all()
    )
    return render_template("index.html", experiences=experiences, timeline=timeline_events)

