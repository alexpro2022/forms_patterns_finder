from tests import conftest as c
PATTERN_NAME = "pattern_name"

#=== ШАБЛОН НАЙДЕН - возвращаем имя шаблона ==========================================================
#--- 1. Полное совпадение присланной формы и шаблона ---
FULL_MATCH_PAYLOAD = [
    {
        "username": "username",
        "password": "password",
        "email": "username111@gmail.com",
        "phone": "+7 999 888 77 55",
        "dob": "2022-12-31"
    },
    {
        "username": "username",
        "password": "password"
    },
    {
        "username": "username",
        "comment": "comment",
        "date": "2022-12-30"
    }
]
FULL_MATCH_SET = (
    (FULL_MATCH_PAYLOAD[0], {PATTERN_NAME: "SignUp"}),
    (FULL_MATCH_PAYLOAD[1], {PATTERN_NAME: "Login"}),
    (FULL_MATCH_PAYLOAD[2], {PATTERN_NAME: "Submit_comment"}),
)

#--- 2. Полей формы больше , чем у шаблона - шаблон "Login" соответствует ---
GREATER_FIELDS_MATCH_PAYLOAD = {
    "username": "username",
    "password": "password",
    "email": "username111@gmail.com",
    "phone": "+7 999 888 77 55",
}
GREATER_FIELDS_MATCH_SET = (
    (GREATER_FIELDS_MATCH_PAYLOAD, {PATTERN_NAME: "Login"}),
)

#--- 3. Подходит более одного шаблона - "SignUP" и "Login" ---
BEST_MATCH_FIELDS_PAYLOAD = {
    "username": "username",
    "password": "password",
    "email": "username111@gmail.com",
    "phone": "+7 999 888 77 55",
    "dob": "2022-12-31",
    "extra_field": "+7 999 888 77 33"
}
BEST_MATCH_SET = (
    (BEST_MATCH_FIELDS_PAYLOAD, {PATTERN_NAME: "SignUp"}),
)


#=== ШАБЛОН НЕ НАЙДЕН - возвращаем ответ в формате: ==========================================================
#    {
#        f_name1: FIELD_TYPE,
#        f_name2: FIELD_TYPE
#    }
#--- Полное несовпадение присланной формы и шаблона
FULL_MISMATCH_PAYLOAD = {
    "username_MISMATCH": "+7 999 888 77 55",
    "password_MISMATCH": "2022-12-27"
}  
FULL_MISMATCH_EXPECTED = {
    "username_MISMATCH": c.PHONE_NUMBER_TYPE,
    "password_MISMATCH": c.DATE_TYPE
}    
FULL_MISMATCH_SET = (
    (FULL_MISMATCH_PAYLOAD, FULL_MISMATCH_EXPECTED),
) 

# --- Частичное совпадение: имя одного поля не совпадает
FIELD_NAME_MISMATCH_PAYLOAD = [
    {
        "username_MISMATCH": "username",
        "password": "password",
        "email": "username111@gmail.com",
        "phone": "+7 999 888 77 55",
        "dob": "2022-12-31"
    },
    {
        "username_MISMATCH": "username",
        "password": "password"
    },
    {
        "username": "username",
        "comment": "comment",
        "date_MISMATCH": "2022-12-30"
    }
]
FIELD_NAME_MISMATCH_EXPECTED = [
    {
        "username_MISMATCH": c.TEXT_TYPE,
        "password": c.TEXT_TYPE,
        "email": c.EMAIL_TYPE,
        "phone": c.PHONE_NUMBER_TYPE,
        "dob": c.DATE_TYPE
    },
    {
        "username_MISMATCH": c.TEXT_TYPE,
        "password": c.TEXT_TYPE
    },
    {
        "username": c.TEXT_TYPE,
        "comment": c.TEXT_TYPE,
        "date_MISMATCH": c.DATE_TYPE
    }
]
FIELD_NAME_MISMATCH_SET = [
    (FIELD_NAME_MISMATCH_PAYLOAD[0], FIELD_NAME_MISMATCH_EXPECTED[0]),
    (FIELD_NAME_MISMATCH_PAYLOAD[1], FIELD_NAME_MISMATCH_EXPECTED[1]),
    (FIELD_NAME_MISMATCH_PAYLOAD[2], FIELD_NAME_MISMATCH_EXPECTED[2]),
]

# --- Частичное совпадение: тип значения одного поля не совпадает
FIELD_VALUE_MISMATCH_PAYLOAD = [
    {
        "username": "2022-12-29",
        "password": "password",
        "email": "username111@gmail.com",
        "phone": "+7 999 888 77 55",
        "dob": "2022-12-31"
    },
    {
        "username": "username",
        "password": "+7 999 888 77 55"
    },
    {
        "username": "username",
        "comment": "comment",
        "date": "+7 999 888 77 55"
    }
]
FIELD_VALUE_MISMATCH_EXPECTED = [
    {
        "username": c.DATE_TYPE,
        "password": c.TEXT_TYPE,
        "email": c.EMAIL_TYPE,
        "phone": c.PHONE_NUMBER_TYPE,
        "dob": c.DATE_TYPE
    },
    {
        "username": c.TEXT_TYPE,
        "password": c.PHONE_NUMBER_TYPE
    },
    {
        "username": c.TEXT_TYPE,
        "comment": c.TEXT_TYPE,
        "date": c.PHONE_NUMBER_TYPE
    }
]
FIELD_VALUE_MISMATCH_SET = (
    (FIELD_VALUE_MISMATCH_PAYLOAD[0], FIELD_VALUE_MISMATCH_EXPECTED[0]),
    (FIELD_VALUE_MISMATCH_PAYLOAD[1], FIELD_VALUE_MISMATCH_EXPECTED[1]),
    (FIELD_VALUE_MISMATCH_PAYLOAD[2], FIELD_VALUE_MISMATCH_EXPECTED[2]),

)
