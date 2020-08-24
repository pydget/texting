from texting import LF, camel_to_snake, snake_to_camel, snake_to_pascal

candidates = {
    'onlyDash': '-._',
    'wsjSnake': 'THE_WALL_STREET_JOURNAL',
    'nytPascal': 'NewYorkTimesFW_2ND',
    'dorian': 'theHurricaneDorianNE1passes',
    'initials': 'A-B-C.BETA',
    'jdwKebab': 'janes-defense-weekly',
    'cp2077': 'THE_CYBER-PUNK.2077 cdpr',
    'dior': 'ChristianDiorSS21'
}


def test():
    print(LF, 'camel_to_snake')
    for key, word in candidates.items():
        print(key, ':', word, '->', camel_to_snake(word))

    print(LF, 'snake_to_camel')
    for key, word in candidates.items():
        print(key, ':', word, '->', snake_to_camel(word))

    print(LF, 'snake_to_pascal')
    for key, word in candidates.items():
        print(key, ':', word, '->', snake_to_pascal(word))


test()
