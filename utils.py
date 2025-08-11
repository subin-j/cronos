from constants import *


# This just checks allowed symbols and expected field length from user input
def validate_input_string(parts: dict) -> bool:
    if not len(parts) == len(FIELD_DICT):
        raise ValueError(
            f"Expected {len(FIELD_DICT)} tokens (5 fields + command), {len(parts)} given."
        )

    for field, expr in parts.items():
        if field == "command":
            continue
        allowed = FIELD_DICT[field]["allowed_symbols"]
        for char in expr:
            if not char.isdigit() and char not in allowed:
                raise ValueError(f"{field}: symbol '{char}' is not allowed")


class Parser:
    def parse_expression(self, field_name: str, expr: str) -> list:
        field_range = FIELD_DICT[field_name]["range"]
        filtered_values = self.parse_field(field_name, expr, field_range)
        return sorted(filtered_values)

    def parse_field(self, field_name: str, expr: str, field_range: list) -> list:
        values = []
        min_range, max_range = field_range[0], field_range[1] + 1

        # 1) "," : when we encounter OR separator,
        # we recursively call parse_field on each expression and union merge the results.
        if RULE_OR in expr:
            union_vals = set()
            for part in expr.split(","):
                part = part.strip()
                union_vals.update(self.parse_field(field_name, part, field_range))
            return list(union_vals)

        # 2) "*"
        if expr == RULE_WILDCARD:
            values = [n for n in range(min_range, max_range)]

        # 3) "*/n" or "start/n"
        elif RULE_STEP in expr:
            ret = self._handle_step(field_name, expr, min_range, max_range)
            values.extend(ret)

        # 4) "a-b"
        elif RULE_RANGE_SEPARATOR in expr:
            ret = self._handle_range(field_name, expr, min_range, max_range)
            values.extend(ret)

        # 5) At this point all values should be filtered.
        # Final range validation and return filtered values.
        else:
            v = int(expr)
            if v < min_range or v >= max_range:
                raise ValueError(
                    f"{field_name}: value {v} out of range [{min_range}-{max_range-1}]"
                )
            values.append(v)
        return values

    @staticmethod
    def _handle_step(
        field_name: str, expr: str, min_range: int, max_range: int
    ) -> list:
        start_str, step_str = expr.split("/", 1)

        # */step
        if start_str == RULE_WILDCARD:
            start = min_range
        # n/step
        else:
            start = int(start_str)

        step = int(step_str)
        if step < 1:
            raise ValueError(f"{field_name}: step must be >= 1")

        # Validate range start is  are within accepted range.
        if not (min_range <= start < max_range):
            raise ValueError(
                f"{field_name}: start {start} out of range [{min_range}-{max_range-1}]"
            )
        return [n for n in range(start, max_range, step)]

    @staticmethod
    def _handle_range(
        field_name: str, expr: str, min_range: int, max_range: int
    ) -> list:
        start_str, end_str = expr.split("-", 1)
        start = int(start_str)
        end = int(end_str)

        if start > end:
            raise ValueError(f"{field_name}: Invalid range: start is bigger than end.")
        if start < min_range or end >= max_range:
            raise ValueError(
                f"{field_name}: range {start}-{end} is out of bounds [{min_range}-{max_range-1}.]"
            )
        return [n for n in range(start, end + 1)]
