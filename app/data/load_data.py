from . import types as t

# !!! Do not change as it is used in tests
PATTERNS = [
    {
        "name": "SignUp",
        "username": t.TEXT_TYPE,
        "password": t.TEXT_TYPE,
        "email": t.EMAIL_TYPE,
        "phone": t.PHONE_NUMBER_TYPE,
        "dob": t.DATE_TYPE
    },
    {
        "name": "Login",
        "username": t.TEXT_TYPE,
        "password": t.TEXT_TYPE
    },
    {
        "name": "Submit_comment",
        "username": t.TEXT_TYPE,
        "comment": t.TEXT_TYPE,
        "date": t.DATE_TYPE
    }
]
