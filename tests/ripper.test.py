from texting import ripper, split_literal
from texting.enum.regexes import LITERAL

print(ripper(LITERAL, "- Friends, Romans, countrymen, lend me your ears -"))

print(split_literal("- Friends, Romans, countrymen, lend me your ears -"))
