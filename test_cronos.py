from cronos import parse_cron_expression

def test_parse_cron_expression():
    expr = "*/5 0 1,15 * 1-5"
    result = parse_cron_expression(expr)
    expected = [
        "*/5",  # minute
        "0",    # hour
        "1,15", # day of month
        "*",    # month
        "1-5"   # day of week
    ]
    assert result == expected
