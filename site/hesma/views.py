"""Additional views."""

from flask import Blueprint, abort, render_template
from invenio_pages.records.models import PageModel


def _render_page(url):
    """Look up a PageModel by URL and render it, or 404 if missing."""
    page = PageModel.query.filter_by(url=url).first()
    if page is None:
        abort(404)
    return render_template(page.template_name, page=page)


#
# Registration
#
def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "hesma",
        __name__,
        template_folder="./templates",
    )

    # Add URL rules
    @blueprint.route("/legalnotice")
    def legal_notice():
        return _render_page("/legalnotice")

    @blueprint.route("/privacy")
    def privacy_policy():
        return _render_page("/privacy")

    return blueprint
