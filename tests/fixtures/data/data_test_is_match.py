from tests import conftest as c

pattern1 = c.PATTERNS[0]
pattern2 = c.PATTERNS[1]
pattern3 = c.PATTERNS[2]

data = (  # pattern, form_data, expected
    (pattern1, pattern1, True),
    (pattern1, pattern2, False),
    (pattern1, pattern3, False),
    (pattern2, pattern1, True),
    (pattern2, pattern2, True),
    (pattern2, pattern3, False),
    (pattern3, pattern1, False),
    (pattern3, pattern2, False),
    (pattern3, pattern3, True),
)
