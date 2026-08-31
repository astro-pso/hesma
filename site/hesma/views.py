"""Additional views."""

from flask import Blueprint, render_template


def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "hesma",
        __name__,
        static_folder="./static",
        static_url_path="/static/hesma",
        template_folder="./templates",
    )

    @blueprint.route("/legalnotice")
    def legal_notice():
        return render_template("hesma/legalnotice.html")

    @blueprint.route("/privacy")
    def privacy_policy():
        return render_template("hesma/privacy.html")

    return blueprint