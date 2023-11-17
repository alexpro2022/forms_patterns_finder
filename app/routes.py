from app.views import forms_view


def setup_routes(app):
    app.router.add_post("/get_form", forms_view)
