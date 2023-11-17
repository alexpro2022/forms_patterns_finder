from app.views import forms_view, index


def setup_routes(app):
    app.router.add_get("/get_form", index)
    app.router.add_post("/get_form", forms_view)
