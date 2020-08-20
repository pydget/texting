import re

from texting import ripper
from texting.enum.regexes import LITERAL

LITERAL_INSTANCE = re.compile(LITERAL)

print(ripper(LITERAL_INSTANCE, "- Friends, Romans, countrymen, lend me your ears -"))
