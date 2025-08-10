from constants import *

from utils import Validator


class Cronos:
    def __init__(self):
        self.field_range = FIELD_RANGE
        self.validator = Validator()

    def run_cronos(self, input_expression: str) -> str:
        # Step 1. Convert input string into map containing key value of field name and expression.
        parsed_map = self._parse_input_expression(input_expression)

        # Step 2. Create map of field as key and list filtered expressions as value.
        filtered_map = self._expand_expressions(parsed_map)

        # Step 3. Build out the output string.
        return self._build_cron_table(filtered_map)

    def _parse_input_expression(self, expr: str) -> dict:
        parts = expr.split()
        self.validator.validate_input_string(parts)
        return {
            FIELD_ORDER[0]: parts[0],
            FIELD_ORDER[1]: parts[1],
            FIELD_ORDER[2]: parts[2],
            FIELD_ORDER[3]: parts[3],
            FIELD_ORDER[4]: parts[4],
            FIELD_ORDER[5]: " ".join(parts[5:]),
        }

    def _expand_expressions(self, parsed_fields: dict) -> dict:
        result = {}
        for field_name, field_expr in parsed_fields.items():
            if field_name == "command":
                result[field_name] = field_expr
            else:
                min_val, max_val = self.field_range[field_name]
                result[field_name] = self._parse_expression(
                    field_expr, min_val, max_val
                )

        return result

    def _parse_expression(self, expr: str, min_val: int, max_val: int) -> list:
        if expr == RULE_WILDCARD:
            return [n for n in range(min_val, max_val + 1)]
        elif expr.startswith(RULE_WILDCARD_STEP):
            step = int(expr.split("/", 1)[1])
            return [n for n in range(min_val, max_val + 1, step)]
        elif RULE_LIST_SEPARATOR in expr:
            return [int(n) for n in expr.split(RULE_LIST_SEPARATOR)]
        elif RULE_RANGE_SEPARATOR in expr:
            start, end = expr.split(RULE_RANGE_SEPARATOR, 1)
            return [n for n in range(int(start), int(end) + 1)]
        else:
            return [int(expr)]

    def _build_cron_table(self, expanded: dict) -> str:
        rows = []
        for name in FIELD_ORDER:
            left = f"{name:<{FIELD_NAME_WIDTH}}"
            if name == FIELD_ORDER[5]:
                rows.append(f"{left}{expanded[name]}")
            else:
                rows.append(f"{left}{' '.join(str(v) for v in expanded[name])}")
        return "\n".join(rows)
