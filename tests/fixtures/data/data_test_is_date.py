data = (
    # --- DD.MM.YYYY ---
    ('31.12.2022', True),
    ('31-12-2022', False),
    ('12-31-2022', False),
    # --- YYYY-MM-DD ---
    ('2022-12-31', True),
    ('2022.12.31', False),
    ('2022-31-12', False),
    # ------------------
    ('asd', False),
)
