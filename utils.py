class Validator:
    def __init(self):
        pass

    def validate_input_string(
        self, parts: list[str], expected_token_length: int = 6
    ) -> None:
        if len(parts) is not expected_token_length:
            raise ValueError(
                f"Expected {expected_token_length} tokens (5 fields + command), {len(parts)} given."
            )
