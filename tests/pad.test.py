from texting import to_pad

candidates = [
    '1',
    '+2.0)',
    'foo'
]

pad = to_pad(ansi=True)
for k in candidates:
    print(pad(k, 3, k))
