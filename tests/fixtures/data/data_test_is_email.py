data = (
    ('username2022@yandex.ru', True),
    ('username2022@gmail.com', True),
    ('2022username2022@yandex.ru', True),
    ('username.2022@gmail.com', True),
    ('2022_username_2022@yandex.ru', True),
    ('_2022_username_2022@yandex.ru', True),
    # -------------------------------------
    ('2022.username.2022@yandex.ru', False),
    ('.2022_username_2022@yandex.ru', False),
    ('2022_username_2022.yandex.ru', False),
    ('2022_username_2022@yandex.r', False),
    ('2022_username_2022@yandex.ruru', False),
)
