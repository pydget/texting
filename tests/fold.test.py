import re

from texting import LF, SP, br
from texting.fold import fold

candidates = {
    'Modigliani': 'What is the "cost of capital" to a, firm in a world in which funds are used to acquire assets whose yields are uncertain; and in which capital can be obtained by many different media, ranging from pure debt instruments, representing money-fixed claims, to pure equity issues, giving holders only the right to a pro-rata share in the uncertain venture? This question has vexed at least three classes of economists: \n(1) the corporation finance specialist concerned with the techniques of financing firms so as to ensure their survival and growth; \n(2) the managerial economist concerned with capital budgeting; and \n(3) the economic theorist concerned with explaining investment behavior at both the micro and macro levels.',
    'Shakes': re.sub(
        '(?<=\w)([.,;:?!])(?=\w)',
        lambda m: m.groups()[0] + LF,
        'Friends, Romans, countrymen, lend me your ears;I come to bury Caesar, not to praise him.The evil that men do lives after them;The good is oft interred with their bones.'
    ),
    'Url': 'click for more: https://www.express.co.uk/news/world/1314688/world-war-3-russia-Vladimir-Putin-navy-parade-st-Petersburg-Moscow-news',
    'LineVoid': 'start' + SP * 82 + LF + 'cyberpunk',
    'LineDash': 'start' + SP + 'a' * 164 + LF + 'cyberpunk',
    'Void': '',
    'Space': ' ',
    'Initial': 'UNESCO',
    'Foo_Bar': 'FOO BAR',
}


def test():
    for key, text in candidates.items():
        print(br(key), fold(text, first_line_indent=len(key) + 3))
        print('-' * 80)


test()
