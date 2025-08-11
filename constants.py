RULE_WILDCARD = "*"
RULE_STEP = "/"
RULE_OR = ","
RULE_RANGE_SEPARATOR = "-"

COMMON_ALLOWED_SYMBOLS = [
    RULE_WILDCARD,
    RULE_STEP,
    RULE_OR,
    RULE_RANGE_SEPARATOR,
]


FIELD_DICT = {
    "minute": {"range": [0, 59], "order": 0, "allowed_symbols": COMMON_ALLOWED_SYMBOLS},
    "hour": {"range": [0, 23], "order": 1, "allowed_symbols": COMMON_ALLOWED_SYMBOLS},
    "day of month": {
        "range": [1, 31],
        "order": 2,
        "allowed_symbols": COMMON_ALLOWED_SYMBOLS,
    },
    "month": {"range": [1, 12], "order": 3, "allowed_symbols": COMMON_ALLOWED_SYMBOLS},
    "day of week": {
        "range": [0, 6],
        "order": 4,
        "allowed_symbols": COMMON_ALLOWED_SYMBOLS,
    },
    "command": {"range": None, "order": 5, "allowed_symbols": []},
}

FIELD_NAME_WIDTH = 14
