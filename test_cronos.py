import pytest
from cronos import parse_input_expression

# expr = "*/15 0 1,15 * 1-5 /usr/bin/find"

# {
#     "minute": "*/15",
#     "hour": "0",
#     "day of month": "1,15",
#     "month": "*",
#     "day of week": "1-5",
#     "command": "/usr/bin/find",
# }

# {
#     "minute": [0, 15, 30, 45],
#     "hour": [0],
#     "day of month": [1, 15],
#     "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#     "day of week": [1, 2, 3, 4, 5],
#     "command": ["/usr/bin/find"],
# }


# 1. INPUT VALIDATION
def test_parse_input_expression():
    expr = "*/5 0 1,15 * 1-5 /usr/bin/find"
    actual = parse_input_expression(expr)
    expected = {
        "minute": "*/5",
        "hour": "0",
        "day of month": "1,15",
        "month": "*",
        "day of week": "1-5",
        "command": "/usr/bin/find",
    }
    assert actual == expected


def test_expand_expressions():
    pass


def test_parse_expression():
    pass


def test_build_and_print_table():
    pass


def test_cron_end_to_end():
    pass
