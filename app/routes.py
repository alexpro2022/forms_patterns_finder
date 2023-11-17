from app.views import forms_view, hello


def setup_routes(app) -> None:
    app.router.add_get('/get_form', hello)
    app.router.add_post('/get_form', forms_view)
