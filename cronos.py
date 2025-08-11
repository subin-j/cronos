from constants import *

from utils import *


class Cronos:
    def __init__(self, input_expr):
        self.input_expr = input_expr
        self.field_dict = FIELD_DICT
        self.parser = Parser()

    def run_cronos(self) -> str:
        # Step 1. Convert input string into map containing key value of field name and expression.
        # "*/15 0 1,15 * 1-5 /usr/bin/find" -> {"minute": "*/15" ...}
        field_expr_map = self._parse_input_expression()

        # Step 2. Create map of field as key and list filtered expressions as value.
        # {"minute": "*/15" ...} -> {"minute":[0,15,30,45 ]....}
        filtered_map = self._expand_expressions(field_expr_map)

        # Step 3. Build out the output string.
        print(self._build_cron_table(filtered_map))

    def _parse_input_expression(self) -> dict:
        expressions = self.input_expr.split()
        field_expr_map = {}
        field_names = [field_name for field_name in self.field_dict.keys()]

        for field_name, expr in zip(field_names, expressions):
            field_expr_map[field_name] = expr
        validate_input_string(field_expr_map)

        print(field_expr_map)
        return field_expr_map

    def _expand_expressions(self, field_expr_map: dict) -> dict:
        for field_name, expr_str in field_expr_map.items():
            if field_name == "command":
                field_expr_map[field_name] = expr_str
            else:
                filtered_value = self.parser.parse_expression(field_name, expr_str)
                field_expr_map[field_name] = filtered_value
        return field_expr_map

    def _build_cron_table(self, expanded: dict) -> str:
        rows = []
        field_names = [field_name for field_name in self.field_dict.keys()]
        for name in field_names:
            line = name + " " * (FIELD_NAME_WIDTH - len(name))
            if name == "command":
                rows.append(line + expanded[name])
            else:
                merged_value_str = " ".join(str(v) for v in expanded[name])
                rows.append(line + merged_value_str)
        return "\n".join(rows)
