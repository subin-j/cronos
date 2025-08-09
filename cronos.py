from pprint import pprint

RANGE = {
    "minute": (0, 59),
    "hour": (0, 23),
    "day of month": (1, 31),
    "month": (1, 12),
    "day of week": (0, 6),
}


def run_cronos(input_expression: str):

    # Step 1. Convert input string into map containing key value of field name and expression
    parsed_map = parse_input_expression(input_expression)

    # Step 2. Do the filtering for each expression value
    # {"minute": "*/5" ...} -> {"minute": [0,15,30,45] ...}
    filtered_map = expand_expressions(parsed_map)

    # Step 3. Build out the output string
    build_and_print_table(filtered_map)


def parse_input_expression(expr: str) -> dict:
    parsed = expr.split(" ")
    parsed_fields = {
        "minute": parsed[0],
        "hour": parsed[1],
        "day of month": parsed[2],
        "month": parsed[3],
        "day of week": parsed[4],
        "command": parsed[5],
    }
    return parsed_fields


def expand_expressions(parsed_fields: dict) -> dict:
    result = {}
    for field_name, field_expr in parsed_fields.items():
        if field_name == "command":
            result[field_name] = [field_expr]
        else:
            min_val, max_val = RANGE[field_name]
            result[field_name] = parse_expression(field_expr, min_val, max_val)

    return result


# input_example= "*/15 0 1,15 * 1-5 /usr/bin/find"
CHAR_SET = {"ALL": "*", "ALL_WITH_STEP": "*/", "OR": ",", "INTERVAL": "-"}


def parse_expression(expr: str, min_val: int, max_val: int) -> list:
    if expr == CHAR_SET["ALL"]:
        return [n for n in range(min_val, max_val + 1)]

    elif expr.startswith(CHAR_SET["ALL_WITH_STEP"]):
        step = int(expr.split("/")[1])
        return [n for n in range(min_val, max_val + 1, step)]

    elif CHAR_SET["OR"] in expr:
        return expr.split(",")

    elif CHAR_SET["INTERVAL"] in expr:
        start, end = expr.split("-")
        return [n for n in range(int(start), int(end) + 1)]
    else:
        return [int(expr)]


def build_and_print_table(expanded):
    # to be implemented
    pprint(expanded)
