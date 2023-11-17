def info(obj, raise_assert: bool = True):
    if hasattr(obj, '__dict__'):
        obj = f'!!!__dict__: {vars(obj)}'
    print(obj)
    if raise_assert:
        assert 0
