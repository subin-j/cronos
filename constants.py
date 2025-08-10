# ---- Field names ----
FIELD_MINUTE = "minute"
FIELD_HOUR = "hour"
FIELD_DAY_OF_MONTH = "day of month"
FIELD_MONTH = "month"
FIELD_DAY_OF_WEEK = "day of week"
FIELD_COMMAND = "command"

FIELD_ORDER = (
    FIELD_MINUTE,
    FIELD_HOUR,
    FIELD_DAY_OF_MONTH,
    FIELD_MONTH,
    FIELD_DAY_OF_WEEK,
    FIELD_COMMAND,
)

# ---- Ranges per field ----
FIELD_RANGE = {
    FIELD_MINUTE: (0, 59),
    FIELD_HOUR: (0, 23),
    FIELD_DAY_OF_MONTH: (1, 31),
    FIELD_MONTH: (1, 12),
    FIELD_DAY_OF_WEEK: (0, 6),
}

# ---- Expression rule symbols ----
RULE_WILDCARD = "*"  # e.g., "*"
RULE_WILDCARD_STEP = "*/"  # e.g., "*/5"
RULE_LIST_SEPARATOR = ","  # e.g., "1,3,5"
RULE_RANGE_SEPARATOR = "-"  # e.g., "1-5"


# ---- Output formatting ----
FIELD_NAME_WIDTH = 14
VALUE_SEPARATOR = " "
