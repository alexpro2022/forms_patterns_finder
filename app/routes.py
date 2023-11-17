from app.views import forms_view


def setup_routes(app) -> None:
    app.router.add_post('/get_form', forms_view)
