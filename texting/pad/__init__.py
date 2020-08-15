def lpad(text: str, width: int, fill: str = ' '):
    return f'{text:{fill[0]}>{width}}'


def rpad(text: str, width: int, fill: str = ' '):
    return f'{text:{fill[0]}<{width}}'


def mpad(text: str, width: int, fill: str = ' '):
    return f'{text:{fill[0]}^{width}}'
