INIWORD = '[A-Za-z\d]+'
INILOW = '^[a-z]+'
CAMEL = '[A-Z]+|[0-9]+'
LITERAL = '[a-z]+|[A-Z][a-z]+|(?<=[a-z]|\W|_)[A-Z]+(?=[A-Z][a-z]|\W|_|$)|[\d]+[a-z]*'
WORD = '[A-Za-z\d]+'
CAPWORD = '[A-Z][a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|_|$)|[\d]+[a-z]*'
DASH_CAPREST = '[\W_]+([A-Za-z\d])([A-Za-z\d]*)'
CAPREST = '([A-Za-z\d])([A-Za-z\d]*)'
