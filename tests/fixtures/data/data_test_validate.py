from tests import conftest as c

data = (
    #--- DD.MM.YYYY ---
    ('31.12.2022', c.DATE_TYPE),
    ('31-12-2022', c.TEXT_TYPE),
    ('12-31-2022', c.TEXT_TYPE),
    #--- YYYY-MM-DD ---
    ('2022-12-31', c.DATE_TYPE),
    ('2022.12.31', c.TEXT_TYPE),
    ('2022-31-12', c.TEXT_TYPE),
    ('asd', c.TEXT_TYPE),     
    #--- +7 xxx xxx xx xx ---       
    ('+7 999 999 99 99', c.PHONE_NUMBER_TYPE),
    # -----------------------
    ('+7-999-999-99-99', c.TEXT_TYPE),    
    ('+7 999 999 9999', c.TEXT_TYPE),
    ('7 999 999 9999', c.TEXT_TYPE),
    ('8 999 999 9999', c.TEXT_TYPE),        
    # --- EMAIL ----------------------------
    ('username2022@yandex.ru', c.EMAIL_TYPE),
    ('username2022@gmail.com', c.EMAIL_TYPE),
    ('2022username2022@yandex.ru', c.EMAIL_TYPE),
    ('username.2022@gmail.com', c.EMAIL_TYPE),
    ('2022_username_2022@yandex.ru', c.EMAIL_TYPE),
    ('_2022_username_2022@yandex.ru', c.EMAIL_TYPE),
    # -------------------------------------
    ('2022.username.2022@yandex.ru', c.TEXT_TYPE),
    ('.2022_username_2022@yandex.ru', c.TEXT_TYPE),
    ('2022_username_2022.yandex.ru', c.TEXT_TYPE),
    ('2022_username_2022@yandex.r', c.TEXT_TYPE),
    ('2022_username_2022@yandex.ruru', c.TEXT_TYPE),
)