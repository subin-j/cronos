import sys
import pytest

from cronos import Cronos
from utils import Parser, validate_input_string
from constants import FIELD_DICT
import cli


def test_cronos_end_to_end_happy(capsys):
    input_expr = "*/15 0 1,15 * 1-5 /usr/bin/find"
    cronos = Cronos(input_expr)

    field_map = cronos._parse_input_expression()
    assert field_map["minute"] == "*/15"
    assert field_map["hour"] == "0"
    assert field_map["day of month"] == "1,15"
    assert field_map["month"] == "*"
    assert field_map["day of week"] == "1-5"
    assert field_map["command"] == "/usr/bin/find"

    expanded = cronos._expand_expressions(field_map)
    assert expanded["minute"] == [0, 15, 30, 45]
    assert expanded["hour"] == [0]
    assert expanded["day of month"] == [1, 15]
    assert expanded["month"] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert expanded["day of week"] == [1, 2, 3, 4, 5]
    assert expanded["command"] == "/usr/bin/find"

    output = cronos._build_cron_table(expanded)
    assert "minute        0 15 30 45" in output
    assert "hour          0" in output
    assert "day of month  1 15" in output
    assert "month         1 2 3 4 5 6 7 8 9 10 11 12" in output
    assert "day of week   1 2 3 4 5" in output
    assert "command       /usr/bin/find" in output

    cronos.run_cronos()
    # check the print output too
    captured = capsys.readouterr()
    assert "minute        0 15 30 45" in captured.out
    assert "hour          0" in captured.out
    assert "day of month  1 15" in captured.out
    assert "month         1 2 3 4 5 6 7 8 9 10 11 12" in captured.out
    assert "day of week   1 2 3 4 5" in captured.out
    assert "command       /usr/bin/find" in captured.out


def test_bad_token_count():
    # invalid token count - omit the last field(command)
    fields_wo_command = [k for k in FIELD_DICT.keys()][:-1]
    bad_parts = {field: "*" for field in fields_wo_command}
    with pytest.raises(ValueError):
        validate_input_string(bad_parts)


def test_bad_character_in_expr():
    bad_parts = {field: "*" for field in FIELD_DICT}
    bad_parts["minute"] = "*/1a"
    with pytest.raises(ValueError):
        validate_input_string(bad_parts)


def test_parser_value_out_of_range():
    parser = Parser()
    with pytest.raises(ValueError):
        parser.parse_expression("minute", "99")


def test_parser_bad_step():
    parser = Parser()
    with pytest.raises(ValueError):
        parser.parse_expression("minute", "*/0")  # step < 1


def test_parser_bad_range():
    parser = Parser()
    with pytest.raises(ValueError):
        parser.parse_expression("hour", "10-5")  # start > end
